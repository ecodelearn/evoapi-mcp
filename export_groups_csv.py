#!/usr/bin/env python3
"""Script para exportar todos os grupos para CSV"""

import csv
from datetime import datetime
from group_controller import GroupController

def export_groups_to_csv():
    """Exporta todos os grupos para um arquivo CSV"""
    print("🔍 Buscando todos os grupos da Evolution API...")
    print("=" * 50)
    
    try:
        # Inicializar controller
        gc = GroupController()
        print(f"✅ Controller inicializado")
        print(f"   Base URL: {gc.base_url}")
        print(f"   Instance: {gc.instance_id}")
        
        # Buscar grupos
        print("\n📥 Buscando grupos...")
        groups = gc.fetch_groups()
        print(f"✅ {len(groups)} grupos encontrados!")
        
        # Nome do arquivo CSV com timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"grupos_whatsapp_{timestamp}.csv"
        
        # Criar CSV
        print(f"\n💾 Salvando em {csv_filename}...")
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            
            # Cabeçalho
            writer.writerow(['ID_Grupo', 'Nome_Grupo', 'Data_Exportacao'])
            
            # Dados dos grupos
            export_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            for group in groups:
                writer.writerow([
                    group.group_id,
                    group.name,
                    export_date
                ])
        
        print(f"✅ Arquivo CSV criado com sucesso!")
        print(f"   📄 Arquivo: {csv_filename}")
        print(f"   📊 Total de grupos: {len(groups)}")
        
        # Mostrar preview dos primeiros grupos
        print(f"\n📋 Preview (primeiros 10 grupos):")
        print("-" * 60)
        for i, group in enumerate(groups[:10]):
            print(f"{i+1:2d}. {group.name}")
            print(f"    ID: {group.group_id}")
            print()
        
        if len(groups) > 10:
            print(f"... e mais {len(groups) - 10} grupos no arquivo CSV")
        
        return csv_filename, len(groups)
        
    except Exception as e:
        print(f"❌ Erro durante a exportação: {e}")
        import traceback
        traceback.print_exc()
        return None, 0

if __name__ == "__main__":
    filename, total = export_groups_to_csv()
    
    if filename:
        print(f"\n🎉 Exportação concluída com sucesso!")
        print(f"📄 Arquivo: {filename}")
        print(f"📊 Total: {total} grupos")
    else:
        print(f"\n❌ Falha na exportação!")