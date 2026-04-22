import json
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from core.domain.segments import get_all_segments
def classify_products(input_file="amazon_products_local.json", output_file="amazon_classified.json"):
    with open(input_file, 'r', encoding='utf-8') as f:
        products = json.load(f)
        
    classified = {
        "Consoles": [],
        "Controles": [],
        "Volantes": [],
        "Headsets & Áudio": [],
        "Jogos": [],
        "Acessórios & Hardware": [],
        "Outros": []
    }
    
    for p in products:
        title = p.get("title", "").lower()
        category = None
        
        for segment in get_all_segments():
            cat = segment.classify_category(title)
            if cat:
                category = cat
                break
                
        if not category:
            category = "Outros"
            
        # O usuário pediu para limpar o JSON mantendo nome, link e fotografia no segmento
        classified[category].append({
            "title": p.get("title"),
            "url": p.get("url"),
            "price": p.get("price_current"),
            "rating": p.get("rating"),
            "image": p.get("image", "")
        })
        
    # Limpa as categorias que ficaram vazias para o JSON final ficar enxuto
    classified = {k: v for k, v in classified.items() if len(v) > 0}
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(classified, f, ensure_ascii=False, indent=4)
        
    print(f"Classificação concluída com sucesso! Objeto salvo em {output_file}\n")
    print("Resumo do agrupamento:")
    for cat, items in classified.items():
        print(f" -> {cat}: {len(items)} produtos")

if __name__ == "__main__":
    classify_products()
