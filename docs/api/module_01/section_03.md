# API de desarrollo

Hay muchas APIs de desarrollo que podemos utilizar para interactuar en la internet, vamos a tomar algunas de las más famosas:


- [https://developers.google.com/](https://developers.google.com/)
    - [https://developers.google.com/youtube](https://developers.google.com/youtube)
    - [Gemini AI](https://ai.google.dev/gemini-api/docs)
- [https://developers.meta.com/](https://developers.meta.com/)
    - [https://developers.facebook.com/](https://developers.facebook.com/)
    - [https://developers.facebook.com/docs/whatsapp/](https://developers.facebook.com/docs/whatsapp/)
    - [https://developers.facebook.com/products/instagram](https://developers.facebook.com/products/instagram) 
- [https://developers.tiktok.com/](https://developers.tiktok.com/)
- [https://developer.linkedin.com/](https://developer.linkedin.com/)
- [https://developers.snap.com/](https://developers.snap.com/)
- [https://developer.x.com/en](https://developer.x.com/en)
- [https://developer.pinterest.com/](https://developer.pinterest.com/)
- [https://developers.reddit.com/](https://developers.reddit.com/)
- [https://core.telegram.org/](https://core.telegram.org/)
- [https://developer.apple.com/](https://developer.apple.com/)
- [https://discord.com/developers](https://discord.com/developers)


---

## Google 

---

### Google - Youtube

Podemos interactuar con la **API de YouTube** las cual nos permite:

- acceder a datos
- buscar videos, 
- obtener información de canales, 
- gestionar listas de reproducción y más. 


#### Pasos para interactuar con la API de YouTube:

1. **Crear un proyecto en Google Cloud Console:**
    - Ve a [Google Cloud Console](https://console.cloud.google.com/).
    - Crea un nuevo proyecto o selecciona uno existente.
    - Habilita la **API de YouTube Data API v3** en la sección de "API y servicios".
        - Si no aparece buscala!

2. **Obtenen las credenciales (API Key o OAuth 2.0):**
    - **API Key:** Si solo necesitas acceder a datos públicos (como buscar videos), genera una clave de API en la sección "Credenciales".
        - No olvides poner restricciones!!! Esto te ayudará a evitar mal uso de to API Key en caso de que se filtre por error o descuido.
    - **OAuth 2.0:** Si necesitas acceder a datos privados (como gestionar listas de reproducción de un usuario), configura OAuth 2.0 y obtén un **Client ID** y **Client Secret**.
        - No olvides poner restricciones!!! Esto te ayudará a evitar mal uso de to API Key en caso de que se filtre por error o descuido.

3. **Instala las bibliotecas o herramientas necesarias según tu stack:**
   - Puedes usar bibliotecas oficiales de Google para interactuar con la API en diferentes lenguajes:
     - **Python:** `google-api-python-client`
     - **JavaScript:** `googleapis`
     - **Java:** `Google API Client Library for Java`
   - También puedes hacer solicitudes HTTP directamente usando herramientas como **Postman** o **cURL**.

4. **Listo ya podemos hacer solicitudes a la API:**
   - La API de YouTube utiliza endpoints RESTful. Por ejemplo podemos:

#### Ejemplos

##### 1. **Buscar videos (usando API Key):**
   - Endpoint: `https://www.googleapis.com/youtube/v3/search`
   - Parámetros comunes:
     - `q`: Término de búsqueda.
     - `part`: Especifica los datos que deseas obtener (por ejemplo, `snippet`).
     - `maxResults`: Número máximo de resultados.
     - `key`: Tu clave de API.

```python
import googleapiclient.discovery

api_key = "TU_API_KEY"
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

request = youtube.search().list(
    q="tutorial python",
    part="snippet",
    maxResults=5
)
response = request.execute()

for item in response["items"]:
    print(item["snippet"]["title"])
```

##### 2. **Obtener información de un canal (usando API Key):**
    - Endpoint: `https://www.googleapis.com/youtube/v3/channels`
    - Parámetros comunes:
        - `id`: ID del canal.
        - `part`: Especifica los datos que deseas obtener (por ejemplo, `snippet,statistics`).

**Ejemplo en cURL:**
```bash
curl "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id=UC_x5XG1OV2P6uZZ5FSM9Ttw&key=TU_API_KEY"
```

##### 3. **Gestionar listas de reproducción (usando OAuth 2.0):**

- Endpoint: `https://www.googleapis.com/youtube/v3/playlists`
- Requiere autenticación OAuth 2.0 para acceder a datos privados.

```python
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Configura OAuth 2.0
SCOPES = ["https://www.googleapis.com/auth/youtube"]
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
credentials = flow.run_local_server(port=0)

youtube = build("youtube", "v3", credentials=credentials)

# Crear una lista de reproducción
request = youtube.playlists().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "Mi lista de reproducción",
            "description": "Descripción de la lista",
        },
        "status": {
            "privacyStatus": "private"
        }
    }
)
response = request.execute()
print(response)
```

**Deberemos tomar en cuenta que**

- Para operaciones públicas (como buscar videos), una **API Key** es suficiente.
- Para operaciones privadas (como gestionar listas de reproducción), necesitas **OAuth 2.0**.

#### Documentación oficial

- La documentación completa de la API de YouTube está disponible en: [YouTube Data API v3 Documentation](https://developers.google.com/youtube/v3).


