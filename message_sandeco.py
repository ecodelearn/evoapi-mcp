"""
MessageSandeco
Criada pelo professor Sandeco, 
essa classe é responsável por extrair e 
organizar os dados de uma mensagem recebida pelo WhatsApp.

sandeco@sandeco.com.br

Refatorada por Rafael


Returns:
    _type_: _description_
"""


import base64
from typing import Optional, Dict, Any

class MessageSandeco:
    
    TYPE_TEXT = "conversation"
    TYPE_AUDIO = "audioMessage"
    TYPE_IMAGE = "imageMessage"
    TYPE_DOCUMENT = "documentMessage"
    TYPE_ERROR = "error"
    
    SCOPE_GROUP = "group"
    SCOPE_PRIVATE = "private"
    
    def __init__(self, data):
        self.data = data
        self.extract_common_data()
        self.extract_specific_data()

    def extract_common_data(self):
        """Extrai os dados comuns e define os atributos da classe."""
        self.event = self.data.get("event")
        
        self.instance = self.data.get("instance")
        self.destination = self.data.get("destination")
        self.date_time = self.data.get("date_time")
        self.server_url = self.data.get("server_url")
        self.apikey = self.data.get("apikey")
        

        data_block = self.data.get("data")   
        
        self.message_type = data_block.get("messageType")
        
        self.push_name = data_block.get("pushName")
        self.status = data_block.get("status")
        self.instance_id = data_block.get("instanceId")
        self.source = data_block.get("source")
        self.message_timestamp = data_block.get("messageTimestamp")
        self.sender = data_block.get("sender")  # Disponível apenas para grupos
        
            
        self.key = data_block.get("key")

        # Atributos diretos
        self.remote_jid = self.key.get("remoteJid")
        self.message_id = self.key.get("id")
        self.from_me = self.key.get("fromMe")
        self.participant = self.key.get("participant")  
# Número de quem enviou no grupo

        # Determina o escopo da mensagem
        self.determine_scope()

    def determine_scope(self):
        """Determina se a mensagem é de grupo ou privada e define os atributos correspondentes."""
        if self.remote_jid.endswith("@g.us"):
            self.scope = self.SCOPE_GROUP
            self.group_id = self.remote_jid.split("@")[0]  # ID do grupo
            self.phone = self.participant.split("@")[0] if self.participant else None  # Número do remetente no grupo
        elif self.remote_jid.endswith("@s.whatsapp.net"):
            self.scope = self.SCOPE_PRIVATE
            self.phone = self.remote_jid.split("@")[0]  # Número do contato
            self.group_id = None  # Não é aplicável em mensagens privadas
        else:
            self.scope = "unknown"  # Tipo desconhecido
            self.phone = None
            self.group_id = None

    def extract_specific_data(self):
        
        data_block = self.data.get("data")
        self.message_block = data_block.get("message")
        
        """Extrai dados específicos e os define como atributos da classe."""
        if self.message_type == self.TYPE_TEXT:
            self.extract_text_message()
        elif self.message_type == self.TYPE_AUDIO:
            self.extract_audio_message()
        elif self.message_type == self.TYPE_IMAGE:
            self.extract_image_message()
        elif self.message_type == self.TYPE_DOCUMENT:
            self.extract_document_message()
        elif self.message_type == self.TYPE_ERROR:
            print("Ocorreu um erro ao processar a mensagem")



    def extract_text_message(self):
        """Extrai dados de uma mensagem de texto e define como atributos."""
        
        self.text_message = self.message_block.get("conversation")

    def extract_audio_message(self):
        """Extrai dados de uma mensagem de áudio e define como atributos da classe."""
        audio_data = self.message_block.get("audioMessage")
        self.audio_base64_bytes = self.message_block.get("base64")
        self.audio_url = audio_data.get("url")
        self.audio_mimetype = audio_data.get("mimetype")
        self.audio_file_sha256 = audio_data.get("fileSha256")
        self.audio_file_length = audio_data.get("fileLength")
        self.audio_duration_seconds = audio_data.get("seconds")
        self.audio_media_key = audio_data.get("mediaKey")
        self.audio_ptt = audio_data.get("ptt")
        self.audio_file_enc_sha256 = audio_data.get("fileEncSha256")
        self.audio_direct_path = audio_data.get("directPath")
        self.audio_waveform = audio_data.get("waveform")
        self.audio_view_once = audio_data.get("viewOnce", False)
        
        
    def extract_image_message(self):
        """Extrai dados de uma mensagem de imagem e define como atributos."""
        
        image_data = self.message_block.get("imageMessage")  
        self.image_url = image_data.get("url")
        self.image_mimetype = image_data.get("mimetype")
        self.image_caption = image_data.get("caption")
        self.image_file_sha256 = image_data.get("fileSha256")
        self.image_file_length = image_data.get("fileLength")
        self.image_height = image_data.get("height")
        self.image_width = image_data.get("width")
        self.image_media_key = image_data.get("mediaKey")
        self.image_file_enc_sha256 = image_data.get("fileEncSha256")
        self.image_direct_path = image_data.get("directPath")
        self.image_media_key_timestamp = image_data.get("mediaKeyTimestamp")
        self.image_thumbnail_base64 = image_data.get("jpegThumbnail")
        self.image_scans_sidecar = image_data.get("scansSidecar")
        self.image_scan_lengths = image_data.get("scanLengths")
        self.image_mid_quality_file_sha256 = image_data.get("midQualityFileSha256")
        self.image_base64 = self.data["message"].get("base64")
        
    def extract_document_message(self):
        """Extrai dados de uma mensagem de documento e define como atributos da classe."""
        
        document_data = self.message_block.get("documentMessage")
        
        self.document_url = document_data.get("url")
        self.document_mimetype = document_data.get("mimetype")
        self.document_title = document_data.get("title")
        self.document_file_sha256 = document_data.get("fileSha256")
        self.document_file_length = document_data.get("fileLength")
        self.document_media_key = document_data.get("mediaKey")
        self.document_file_name = document_data.get("fileName")
        self.document_file_enc_sha256 = document_data.get("fileEncSha256")
        self.document_direct_path = document_data.get("directPath")
        self.document_caption = document_data.get("caption", None)
        self.document_base64_bytes = self.decode_base64(self.data["message"].get("base64"))

    def decode_base64(self, base64_string):
        """Converte uma string base64 em bytes."""
        if base64_string:
            return base64.b64decode(base64_string)
        return None

    def get(self):
        """Retorna todos os atributos como um dicionário."""
        return self.__dict__

    def get_text(self):
        """Retorna o texto da mensagem, dependendo do tipo."""
        text = ""
        if self.message_type == self.TYPE_TEXT:
            text = self.text_message
        elif self.message_type == self.TYPE_IMAGE:
            text = self.image_caption
            
        return text


    def get(self) -> Dict[str, Any]:
        """Get all attributes as a dictionary."""
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
    
    
    @staticmethod
    def get_messages(messages):
        """Retorna uma lista de objetos `Message` a partir de uma lista de mensagens."""
        msgs = messages.get('messages').get('records')

        mensagens = []
        for msg in msgs:
            mensagens.append(MessageSandeco(msg))

        return mensagens
