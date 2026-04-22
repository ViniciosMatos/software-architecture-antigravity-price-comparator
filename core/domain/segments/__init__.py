from core.domain.segments.base_segment import ProductSegment
from core.domain.segments.playstation_segment import PlayStationSegment
from core.domain.segments.xbox_segment import XboxSegment

# Facilita a injeção ou descoberta de todos os segmentos ativos
def get_all_segments() -> list[ProductSegment]:
    return [
        PlayStationSegment(),
        XboxSegment(),
    ]
