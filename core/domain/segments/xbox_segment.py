from typing import Optional, List
from core.domain.segments.base_segment import ProductSegment

class XboxSegment(ProductSegment):
    def get_search_urls(self) -> List[str]:
        return [
            "https://www.amazon.com.br/s?k=xbox+one",
        ]
        
    def classify_category(self, title: str) -> Optional[str]:
        t = title.lower()
        
        # Ignora se for PS5
        if "playstation" in t or "ps5" in t or "ps4" in t:
            return None
            
        # Força restrição de segmento usando palavra-chave "xbox" ou "microsoft" para a maioria das peças
        is_xbox_context = "xbox" in t or "microsoft" in t
        
        if is_xbox_context:
            # 1. Acessórios
            if any(x in t for x in ["cabo", "fonte", "bateria", "play and charge", "carregador", "suporte", "hd ", "ssd "]):
                return "Acessórios & Hardware"
                
            # 5. Consoles
            elif any(x in t for x in ["console", "pacote", "bundle", "series s", "series x", "500gb", "1tb", "edição digital", "edicao digital"]):
                return "Consoles"
                
            # 2. Controles
            elif any(x in t for x in ["controle", "controller", "controlador", "gamepad", "joystick"]):
                return "Controles"
                
            # 3. Headset
            elif any(x in t for x in ["headset", "fone"]):
                return "Headsets & Áudio"
                
            # 4. Jogos
            elif any(x in t for x in ["jogo", "game", "simulator", "battle", "edition", "standard", "rehydrated", "mídia física", "cd "]):
                return "Jogos"
                
        # Fallback de marcas terceiras
        if any(x in t for x in ["volante", "g920", "g923"]):
            if "g920" in t or ("g923" in t and is_xbox_context):
                return "Volantes"
                
        return None

    def normalize_variant(self, title: str, category: str) -> Optional[str]:
        t = title.lower()
        
        if category == "Consoles":
            if "xbox one s" in t: return "Console Xbox One S"
            elif "xbox one x" in t: return "Console Xbox One X"
            elif "series x" in t: return "Console Xbox Series X"
            elif "series s" in t: return "Console Xbox Series S"
            elif "xbox one" in t: return "Console Xbox One (Fat/Base)"
            return "Console Xbox Genérico"
            
        elif category == "Controles":
            if "elite" in t: return "Controle Xbox Elite Wireless"
            elif "pulse red" in t or "shock blue" in t or "carbon black" in t or "robot white" in t:
                return "Controle Xbox Wireless (Series/One)"
            return "Controle Xbox Wireless Padrão"
            
        elif category == "Volantes":
            if "g920" in t: return "Volante Logitech G920 (Xbox)"
            elif "g923" in t: return "Volante Logitech G923 (Xbox)"
            return "Volante Xbox Genérico"
            
        elif category == "Headsets & Áudio":
            if "wireless headset" in t and "xbox" in t: return "Xbox Wireless Headset"
            if "g pro x" in t or "g435" in t: return None # Deixa pro PlayStation resolver se bater
            return "Headset Xbox Genérico"
            
        elif category == "Acessórios & Hardware":
            if "play and charge" in t or "bateria" in t: return "Kit Jogar e Carregar Xbox"
            if "fonte" in t and "xbox one" in t: return "Fonte de Alimentação Xbox One"
            return "Acessório Xbox Genérico"
            
        elif category == "Jogos":
            if "game pass" in t or "gamepass" in t: return "Assinatura Xbox Game Pass"
            if "halo" in t: return "Jogo: Halo"
            if "forza" in t: return "Jogo: Forza Horizon / Motorsport"
            if "gears" in t: return "Jogo: Gears of War"
            return "Jogo Xbox Genérico"
            
        return None
