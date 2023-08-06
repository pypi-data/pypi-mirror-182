//! Methods for compressing the posting lists

use std::{
    fs::File,
    io::{Seek, Write},
    path::Path,
};

use super::wand::{WandIndex, WandIterator};
use crate::base::{DocId, ImpactValue};
use sucds::{EliasFanoBuilder, Searial};

pub trait Compressor<T> {
    fn add(&mut self, value: &T);
}

pub trait CompressorFactory<T> {
    fn init<'a>(
        &self,
        value_writer: &'a mut dyn Write,
        it: &dyn WandIterator,
    ) -> Box<dyn Compressor<T> + 'a>;
}

/// Compress the impact values
pub fn compress(
    path: &Path,
    index: &dyn WandIndex,
    doc_compressor_factory: &dyn CompressorFactory<DocId>,
    value_compressor_factory: &dyn CompressorFactory<ImpactValue>,
) -> Result<(), std::io::Error> {
    let mut value_writer = File::options()
        .write(true)
        .truncate(true)
        .create(true)
        .open(path.join("value.dat"))
        .expect("Could not create the values file");
    let mut docid_writer = File::options()
        .write(true)
        .truncate(true)
        .create(true)
        .open(path.join("docid.dat"))
        .expect("Could not create the document IDs file");

    for term_ix in 0..index.length() {
        let mut it = index.iterator(term_ix);
        {
            let mut doc_compressor = doc_compressor_factory.init(&mut value_writer, it.as_ref());
            let mut value_compressor =
                value_compressor_factory.init(&mut docid_writer, it.as_ref());

            while let Some(ti) = it.next() {
                doc_compressor.add(&ti.docid);
                value_compressor.add(&ti.value);
            }
        }
        value_writer.stream_position()?;
        docid_writer.stream_position()?;
    }

    Ok(())
}

// --- Elias Fano

struct EliasFanoCompressor<'a> {
    builder: EliasFanoBuilder,
    writer: &'a mut dyn Write,
}
impl<'a> Compressor<DocId> for EliasFanoCompressor<'a> {
    fn add(&mut self, value: &DocId) {
        self.builder
            .append(&[*value as usize])
            .expect("Could not add a doc ID");
    }
}
impl<'a> Drop for EliasFanoCompressor<'a> {
    fn drop(&mut self) {
        let mut other = EliasFanoBuilder::new(1, 1).expect("Yaaa");
        std::mem::swap(&mut other, &mut self.builder);
        other
            .build()
            .serialize_into(&mut self.writer)
            .expect("Yoooo");
    }
}

struct EliasFanoCompressorFactory {}
impl CompressorFactory<DocId> for EliasFanoCompressorFactory {
    fn init<'a>(
        &self,
        writer: &'a mut dyn Write,
        it: &dyn WandIterator,
    ) -> Box<dyn Compressor<DocId> + 'a> {
        Box::new(EliasFanoCompressor {
            builder: EliasFanoBuilder::new(it.max_doc_id().try_into().unwrap(), it.length())
                .expect("Error when building"),
            writer: writer,
        })
    }
}
