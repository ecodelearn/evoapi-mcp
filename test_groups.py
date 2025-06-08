#!/usr/bin/env python3
"""Teste da funcionalidade get_groups"""

from group_controller import GroupController

def test_get_groups():
    print("🧪 Testando fetch_groups...")
    print("=" * 50)
    
    try:
        # Inicializar controller
        gc = GroupController()
        print(f"✅ Controller inicializado")
        print(f"   Base URL: {gc.base_url}")
        print(f"   Instance: {gc.instance_id}")
        
        # Buscar grupos
        print("\n🔍 Buscando grupos...")
        groups = gc.fetch_groups()
        
        print(f"✅ Sucesso! Encontrados {len(groups)} grupos:")
        print("-" * 30)
        
        for i, group in enumerate(groups[:10]):  # Mostrar apenas os primeiros 10
            print(f"{i+1:2d}. Nome: {group.name}")
            print(f"    ID: {group.group_id}")
            print()
            
        if len(groups) > 10:
            print(f"... e mais {len(groups) - 10} grupos")
            
        return True
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    test_get_groups()