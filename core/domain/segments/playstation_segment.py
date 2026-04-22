import re
from typing import Optional, List
from core.domain.segments.base_segment import ProductSegment

class PlayStationSegment(ProductSegment):
    def get_search_urls(self) -> List[str]:
        return [
            "https://www.amazon.com.br/s?k=playstation+5",
        ]
        
    def classify_category(self, title: str) -> Optional[str]:
        t = title.lower()
        
        # Ignora se for claramente de Xbox (pois os nomes podem colidir as vezes, ex: Volantes)
        if "xbox" in t and "ps5" not in t and "playstation" not in t:
            return None
            
        # As lógicas clássicas de classify_products (Restaurando ao comportamento original!)
        if any(x in t for x in ["volante", "pedais", "driving force", "g923", "g29"]):
            return "Volantes"
            
        elif any(x in t for x in ["headset", "fone", "áudio"]):
            return "Headsets & Áudio"
            
        elif any(x in t for x in ["cabo", "cable", "usb", "suporte", "base", "carregamento", "ssd", "unidade de disco", "vr2", "portal remote", "lcd"]):
            return "Acessórios & Hardware"
            
        elif any(x in t for x in ["console ", "pacote ", "bundle", "edição digital", "digital edition", "disc edition", "disc console"]) and "para console" not in t:
            return "Consoles"
            
        elif "playstation 5 slim" in t or "playstation®5" in t or "playstation 5 pro" in t or "ps5 digital" in t:
            return "Consoles"
            
        elif any(x in t for x in ["controle", "dualsense", "controller", "mando", "joystick"]):
            return "Controles"
            
        elif any(x in t for x in ["jogo", "spider-man", "gran turismo", "ghost of", "resident evil", "pragmata", "mega man", "collection", "game"]):
            return "Jogos"
            
        elif any(x in t for x in ["playstation 5", "playstation®5", "ps5", " ps5 "]) and "para playstation" not in t and "compatível com playstation" not in t and "para ps5" not in t and "compatível com ps5" not in t:
            return "Consoles"
            
        return None

    def normalize_variant(self, title: str, category: str) -> Optional[str]:
        t = title.lower()
        
        # Guard clause: Xbox products should not hit the PlayStation fallback names
        if "xbox" in t and "ps5" not in t and "playstation" not in t:
            return None
            
        if category == "Consoles":
            if re.search(r'\bpro\b', t): return "Console PlayStation 5 PRO"
            elif "slim" in t:
                if "digital" in t or "edição digital" in t or "disk" not in t and "disco" not in t:
                    if "digital" in t or "edição digital" in t:
                        return "Console PlayStation 5 Slim Digital"
                return "Console PlayStation 5 Slim Standard (Disco)"
            elif "digital" in t or "edição digital" in t:
                return "Console PlayStation 5 Base Digital"
            else: return "Console PlayStation 5 Standard (Base/Fat)"
                
        elif category == "Controles":
            if "edge" in t or "pro " in t: return "Controle DualSense Edge (Pro)"
            elif "hori" in t or "luta" in t: return "Controle Fightpad Hori ALPHA"
            elif "dualsense" in t or "controle" in t: return "Controle DualSense Padrão"
            else: return "Controle Genérico"

        elif category == "Volantes":
            if "g29" in t: return "Volante Logitech G29"
            elif "g923" in t: return "Volante Logitech G923"
            elif "direct drive" in t or "g pro" in t or "pro wheel" in t: return "Volante Logitech G PRO Direct Drive"
            else: return "Volante Genérico"

        elif category == "Headsets & Áudio":
            if "g pro x 2" in t: return "Headset Logitech G PRO X 2"
            elif "g435" in t: return "Headset Logitech G435"
            else: return "Headset/Fones Diversos"

        elif category == "Acessórios & Hardware":
            if "portal" in t: return "PlayStation Portal"
            elif "vr2" in t: return "PlayStation VR2"
            elif "unidade de disco" in t or "drive" in t.replace("direct drive", ""): return "Leitor de Disco Avulso PS5"
            elif "base de carregamento" in t or "carregador" in t: return "Base de Carregamento DualSense"
            elif "cabo" in t or "cable" in t: return "Cabo HDMI / USB"
            elif "ssd" in t or "firecuda" in t: return "SSD Interno M.2"
            elif "suporte" in t: return "Suporte Vertical Console"
            else: return "Acessório Genérico"
                
        elif category == "Jogos":
            if "spider-man" in t: return "Jogo: Marvel's Spider-Man 2"
            elif "gran turismo" in t: return "Jogo: Gran Turismo 7"
            elif "ghost of" in t: return "Jogo: Ghost of Tsushima/Yōtei"
            elif "resident evil" in t: return "Jogo: Resident Evil"
            elif "pragmata" in t: return "Jogo: Pragmata"
            elif "mega man" in t: return "Jogo: Mega Man Collection"
            elif "ea sports" in t or "fc" in t: return "Jogo: EA Sports FC"
            else: return "Jogo Genérico"
            
        return None
