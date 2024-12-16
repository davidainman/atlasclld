Instructions for running the ATLAs CLLD application:

1. Subscribe to the atlas-data repository or download a copy.
2. Navigate to the atlasclld folder.
3. From the top-level atlasclld folder, run `pip install -e .[dev]` (on a Mac, `pip install -e ."[dev]"`
4. Run `clld initdb development.ini --cldf path-to-atlas-data/cldf-atlas/StructureDataset-metadata.json`
5. Run `pserve --reload development.ini`
