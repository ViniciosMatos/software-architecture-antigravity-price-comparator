import sqlite3
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from core.domain.segments import get_all_segments
from core.domain.services import ProductDomainService

def update_variant_names():
    conn = sqlite3.connect('amazon_offers_history.db')
    cursor = conn.cursor()

    # Get all entries
    cursor.execute('SELECT id, title, variant_name FROM cheapest_offers_history')
    rows = cursor.fetchall()

    for row in rows:
        id_, title, current_variant = row
        if current_variant.startswith('Outros:'):
            # Try to find correct variant
            category = None
            for segment in get_all_segments():
                cat = segment.classify_category(title)
                if cat:
                    category = cat
                    break
            if category:
                new_variant = ProductDomainService.normalize_product_variant(title, category)
                if new_variant:
                    print(f"Updating {current_variant} to {new_variant}")
                    cursor.execute('UPDATE cheapest_offers_history SET variant_name = ? WHERE id = ?', (new_variant, id_))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    update_variant_names()