

Instalación
pip install pycryptodome
 Uso rápido
Paso 1 (Generar llave): python crypto_tool.py genkey (Crea el archivo key.bin).
Paso 2 (Cifrar): python crypto_tool.py encrypt mensaje_prueba.txt (Crea cifrado.bin).
Paso 3 (Descifrar): python crypto_tool.py decrypt cifrado.bin (Muestra el texto en pantalla).
Detalles Técnicos
Algoritmo: AES.
Modo: EAX.
Justificación: Se eligió porque ofrece autenticación. Si el archivo cifrado se altera aunque sea un bit, el programa lo detecta y no lo descifra (garantiza integridad).
Tamaño de llave: 256 bits (32 bytes).
Justificación: Es el estándar de seguridad más robusto actualmente (AES-256).
