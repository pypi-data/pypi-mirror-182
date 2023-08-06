import abc
from sqlite3 import Connection
from tileset_analyzer.data_source.mbtiles.mbtiles_source import MBTileSource


class TilesetSourceFactory:
    @staticmethod
    def get_tileset_source(src_path: str, scheme: str):
        try:
            if src_path.endswith('mbtiles'):
                return MBTileSource(src_path, scheme)
            
            raise AssertionError("Tileset Type is not valid.")
        except AssertionError as e:
            print(e)
