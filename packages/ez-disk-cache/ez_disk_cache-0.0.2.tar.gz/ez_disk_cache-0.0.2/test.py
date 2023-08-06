from dataclasses import dataclass

from ez_disk_cache import DiskCacheConfig, disk_cache

@dataclass
class CarConfig(DiskCacheConfig):
    model: str
    color: str  # In this example, we neglect 'color' when searching for compatible cache instances

    @staticmethod
    def _cache_is_compatible(passed_to_decorated_function: "CarConfig", loaded_from_cache: "CarConfig") -> bool:
        """Return True, if a cache instance is compatible. False if not."""
        if passed_to_decorated_function.model == loaded_from_cache.model:
            return True
        return False  # At this point, we don't care about 'color'. Everything that matters is 'model'.

