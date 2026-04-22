import re
from core.domain.segments import get_all_segments

class ProductDomainService:
    @staticmethod
    def normalize_product_variant(title: str, category: str) -> str:
        """
        Deduze qual é o modelo base (Variação) do produto baseado no título e categoria.
        Delega a decisão de normalização de acordo com as classes Segment injetadas.
        """
        for segment in get_all_segments():
            variant = segment.normalize_variant(title, category)
            if variant:
                return variant
                
        return f"Outros: {title[:30]}"

    @staticmethod
    def parse_price(price_text: str) -> float:
        """
        Trata e converte a string BRL (ex: 'R$ 4.199,90') para float '4199.90'.
        """
        if not price_text or "sem" in price_text.lower() or "erro" in price_text.lower():
            return 0.0
        
        clean = re.sub(r'[^\d.,]', '', price_text)
        if not clean:
            return 0.0
            
        clean = clean.replace('.', '')
        clean = clean.replace(',', '.')
        
        try:
            return float(clean)
        except ValueError:
            return 0.0
