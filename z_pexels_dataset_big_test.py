import os
import json
import requests
from PIL import Image
from io import BytesIO
from datetime import datetime
import time
import random

# Used to donwload images from Pexels


# --- Config ---
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")  # pexels api key in enviroment variable
TOTAL_IMAGENS = 70  # per emotion
TRAIN_DIR = "./dataset_emocional_local_testBIG200"  # Train directory
TEST_DIR = "./dataset_emocional_local_testTEST70"  # Test Directory
PASTA_IMAGENS_TREINO = os.path.join(TRAIN_DIR, "images")
PASTA_METADATA_TREINO = os.path.join(TRAIN_DIR, "metadata")
PASTA_IMAGENS_TESTE = os.path.join(TEST_DIR, "images")
PASTA_METADATA_TESTE = os.path.join(TEST_DIR, "metadata")

# Emotions and Prompts
EMOTIONS = ["joy", "anger", "fear", "sadness", "surprise", "neutral"]
SYNONYMS = {
    "joy": ["happiness", "delight", "cheerfulness"],
    "anger": ["fury", "ire", "wrath", "irritation"],
    "fear": ["panic"],
    "sadness": ["grief","sorrow","melancholy","heartache"],
    "surprise": ["astonishment","amazement"],
    "neutral": ["blank face","neutral expression","impartiality"],
}
EMOTION_PROMPTS = {
    "joy": "Describe this joyful scene.",
    "anger": "Describe this angry scene.",
    "fear": "Describe this fearful scene.",
    "sadness": "Describe this sad scene.",
    "surprise": "Describe this surprising scene.",
    "neutral": "Describe this scene objectively."
}

# API Config
MAX_RETRIES = 3
REQUEST_DELAY = 1  # delay 
RATE_LIMIT_DELAY = 60  # wait time

# --- Folders ---
os.makedirs(PASTA_IMAGENS_TESTE, exist_ok=True)
os.makedirs(PASTA_METADATA_TESTE, exist_ok=True)

# --- Functions ---
def fazer_requisicao_pexels(url, headers, params):
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url, headers=headers, params=params)
            
            if response.status_code == 429:
                print(f"Rate limit atingido. Esperando {RATE_LIMIT_DELAY} segundos...")
                time.sleep(RATE_LIMIT_DELAY)
                continue
                
            if response.status_code != 200:
                print(f"[ERRO] Pexels {params.get('query', '')} página {params.get('page', 1)}: {response.status_code}")
                return None
                
            return response.json()
            
        except Exception as e:
            print(f"[ERRO] Tentativa {attempt + 1} falhou: {e}")
            time.sleep(REQUEST_DELAY * (attempt + 1))
    
    return None

def buscar_imagens_pexels(query, quantidade):
    imagens = []
    pagina = 1
    max_por_pagina = 80  # Maximum allowed by api
    headers = {"Authorization": PEXELS_API_KEY}
    
    while len(imagens) < quantidade:
        # Calculate how many images to request
        restantes = quantidade - len(imagens)
        per_page = min(restantes, max_por_pagina)
        
        params = {
            "query": query,
            "per_page": per_page,
            "page": pagina
        }
        
        dados = fazer_requisicao_pexels("https://api.pexels.com/v1/search", headers, params)
        if not dados:
            break
            
        novas_imagens = dados.get("photos", [])
        if not novas_imagens:
            break
            
        # Filter duplicates
        for img in novas_imagens:
            pexels_id = img.get("id")
            if not any(i.get("id") == pexels_id for i in imagens):
                imagens.append(img)
        
        # Respect rate limits
        time.sleep(REQUEST_DELAY + random.uniform(0, 0.5)) 
        
        pagina += 1
    
    return imagens[:quantidade]

def baixar_e_salvar_imagem(url, caminho_destino):
    for attempt in range(MAX_RETRIES):
        try:
            resposta = requests.get(url, timeout=10)
            resposta.raise_for_status()
            imagem = Image.open(BytesIO(resposta.content)).convert("RGB")
            imagem.save(caminho_destino)
            return True
        except Exception as e:
            print(f"[ERRO] Tentativa {attempt + 1} falhou ao baixar imagem: {e}")
            time.sleep(REQUEST_DELAY * (attempt + 1))
    return False

def imagem_ja_existe(pexels_id):
    """Verifica se a imagem já existe em qualquer emoção nos conjuntos de treino ou teste"""
    # Verify directories
    pastas = [
        PASTA_IMAGENS_TREINO,
        PASTA_IMAGENS_TESTE,
        PASTA_METADATA_TREINO,
        PASTA_METADATA_TESTE
    ]
    
    for pasta in pastas:
        if not os.path.exists(pasta):
            continue
            
        for arquivo in os.listdir(pasta):
            # Verify identifier
            if str(pexels_id) in arquivo:
                return True
                
            # Verify in metadata content
            if arquivo.endswith('.json'):
                try:
                    with open(os.path.join(pasta, arquivo), 'r') as f:
                        meta = json.load(f)
                        if str(pexels_id) == str(meta.get("pexels_id", "")):
                            return True
                except:
                    continue
    return False

def salvar_dataset_teste():
    total_salvas = 0
    stats = {emotion: 0 for emotion in EMOTIONS}
    
    for emotion in EMOTIONS:
        print(f"\nColetando imagens de teste para: {emotion}")
        imagens_salvas_emoção = 0
        tentativas = 0
        max_tentativas = TOTAL_IMAGENS * 10
        paginas_com_erro = 0
        max_paginas_com_erro = 20
        
        # First try main emotion
        queries_priority = [f"{emotion} emotion face"]
        # After try synonyms
        queries_secondary = [f"{synonym} emotion face" for synonym in SYNONYMS.get(emotion, [])]
        
        while imagens_salvas_emoção < TOTAL_IMAGENS and tentativas < max_tentativas:
            # Mix priority and secondary queries
            current_queries = queries_priority if tentativas < len(queries_priority) * 2 else queries_priority + queries_secondary
            
            # Select query
            if tentativas < len(queries_priority):
                query = queries_priority[tentativas % len(queries_priority)]
            else:
                query = random.choice(current_queries)
            
            lote = min(20, TOTAL_IMAGENS - imagens_salvas_emoção)
            
            # Try different query variations
            if tentativas > TOTAL_IMAGENS * 2:
                query_variations = [
                    f"{query.split()[0]} face expression",
                    f"{query.split()[0]} human face",
                    f"{query.split()[0]} facial expression",
                    f"{query.split()[0]} situation",
                    f"{query.split()[0]} ocasion",
                    f"person {query.split()[0]} emotion"
                ]
                query = random.choice(query_variations)
                print(f"Tentando variação de query: {query}")
            
            imagens = buscar_imagens_pexels(query, lote)
            
            if not imagens:
                print(f"Nenhuma nova imagem encontrada para: {query}")
                tentativas += 1
                paginas_com_erro += 1
                time.sleep(REQUEST_DELAY)
                
                if paginas_com_erro >= max_paginas_com_erro:
                    print(f"Muitas páginas com erro consecutivas. Tentando nova estratégia...")
                    paginas_com_erro = 0
                    tentativas = max(0, tentativas - 10)
                    time.sleep(RATE_LIMIT_DELAY)
                continue
            else:
                paginas_com_erro = 0
                
            for img_info in imagens:
                if imagens_salvas_emoção >= TOTAL_IMAGENS:
                    break
                    
                try:
                    url = img_info["src"]["original"]
                    alt = img_info.get("alt", "")
                    pexels_id = img_info.get("id", f"noid_{time.time()}")
                    
                    if imagem_ja_existe(pexels_id):
                        tentativas += 1
                        continue
                    
                    nome_base = f"{emotion}_{pexels_id}_{imagens_salvas_emoção}"
                    caminho_img = os.path.join(PASTA_IMAGENS_TESTE, f"{nome_base}.jpg")
                    caminho_meta = os.path.join(PASTA_METADATA_TESTE, f"{nome_base}.json")

                    if not baixar_e_salvar_imagem(url, caminho_img):
                        tentativas += 1
                        continue

                    metadado = {
                        "image_path": caminho_img,
                        "emotion": emotion,
                        "prompt": EMOTION_PROMPTS[emotion],
                        "alt_text": alt,
                        "pexels_id": pexels_id,
                        "original_url": url,
                        "timestamp": datetime.now().isoformat(),
                        "is_test": True,
                        "search_query": query
                    }

                    with open(caminho_meta, "w") as f:
                        json.dump(metadado, f, indent=2)

                    print(f"Imagem de teste salva [{imagens_salvas_emoção+1}/{TOTAL_IMAGENS}]: {emotion} (via {query}) - ID {pexels_id}")
                    total_salvas += 1
                    imagens_salvas_emoção += 1
                    stats[emotion] += 1
                    tentativas = 0
                    
                    time.sleep(REQUEST_DELAY + random.uniform(0, 0.3))
                        
                except Exception as e:
                    print(f"[ERRO] Ao processar imagem: {e}")
                    tentativas += 1
                    continue

        print(f"Concluído para {emotion}: {stats[emotion]}/{TOTAL_IMAGENS} imagens")

    print("\nResumo Final:")
    for emotion, count in stats.items():
        print(f"{emotion}: {count}/{TOTAL_IMAGENS}")
    print(f"\nTotal de imagens de teste salvas: {total_salvas}/{TOTAL_IMAGENS*len(EMOTIONS)}")
    print(f"Imagens em: {PASTA_IMAGENS_TESTE}")
    print(f"Metadados em: {PASTA_METADATA_TESTE}")

# --- Execution ---
if __name__ == "__main__":
    # Folder
    if not os.path.exists(PASTA_IMAGENS_TREINO):
        print(f"AVISO: Diretório de treino não encontrado: {PASTA_IMAGENS_TREINO}")
        print("As verificações de duplicatas não incluirão o dataset de treino.")
    
    # API key
    if not PEXELS_API_KEY:
        print("ERRO: Chave da API Pexels não encontrada.")
        print("Defina a variável de ambiente PEXELS_API_KEY ou modifique o código.")
    else:
        salvar_dataset_teste()