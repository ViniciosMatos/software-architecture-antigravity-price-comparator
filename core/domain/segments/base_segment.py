from abc import ABC, abstractmethod
from typing import Optional, List

class ProductSegment(ABC):
    """
    Define o contrato para segmentos independentes de produtos (Ex: PlayStation, Xbox, Nintendo).
    Cada segmento encapsula as regras de busca, classificação e normalização de seu nicho.
    """
    
    @abstractmethod
    def get_search_urls(self) -> List[str]:
        """Retorna a lista de URLs da loja (Amazon) para buscar os produtos desse segmento."""
        pass
        
    @abstractmethod
    def classify_category(self, title: str) -> Optional[str]:
        """
        Analisa o título de um anúncio. 
        Se o produto pertencer exclusivamente a este segmento, retorna sua Categoria Macro 
        (ex: 'Consoles', 'Controles', 'Volantes', 'Jogos').
        Retorna None caso o produto não pertença a este segmento.
        """
        pass
        
    @abstractmethod
    def normalize_variant(self, title: str, category: str) -> Optional[str]:
        """
        Normaliza o nome do modelo/variante exata do produto.
        (ex: 'Console Xbox One S 1TB', 'Controle DualSense Edge').
        Retorna None se não conseguir identificar o padrão dentro de seu segmento.
        """
        pass
