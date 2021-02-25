class script(object):
    START_TEXT = """¡Hola, mi principal función es renombrar archivos!
    	    
<b>¡Envíame cualquier archivo de Telegram y elige la opción que desees!</b>
Escriba /help para más información."""

    RENAME_403_ERR = "Perdón, tú no tienes permitido renombrar este archivo"
    UPGRADE_TEXT = "Habla con @DKzippO para negociar 🌚"
    DOWNLOAD_START = "😌 Intentando descargar a mi base de datos, espere por favor..."
    UPLOAD_START = "<b>😀 La descarga ha terminado, estoy intentando subir el archivo a Telegram...</b>"
    AFTER_SUCCESSFUL_UPLOAD_MSG = "<b>Gracias por usarme 🤓</b>\n Por favor, califícame si me encuentras útil: https://t.me/tlgrmcbot?start=renamearchive_bot-review ❤️"
    SAVED_THUMB = "<b>Miniatura personalizada guardada ✅ Esto es permanente hasta que escribas /delthumb</b>"
    DEL_THUMB = "Miniatura borrada con éxito 🤦"
    NO_THUMB = "No se encontraron miniaturas personalizadas"
    SAVED_RECVD_DOC_FILE = "<b>Archivo descargado correctamente 😎</b>"
    CUSTOM_CAPTION_UL_FILE = "Renombrado con: @RenameArchive_bot ❤️"
    HELP_USER = """<b>El modo de uso del bot es el siguiente 🤓:</b>
    
🔹1. Envíe una foto para usarla como miniatura personalizada.
🔹1. Envíame cualquier archivo de Telegram.
🔹3. Elija la opción adecuada."""
