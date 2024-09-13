from PIL import Image
import numpy as np

def image_to_ascii(img, output_width=150, output_height=None):
    # Caracteres ASCII ordenados por intensidade (pode adicionar mais caracteres para mais detalhes)
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.', ' ']
    
    # Calcular a altura baseada na largura e na razão de aspecto original
    if output_height is None:
        aspect_ratio = img.height / img.width
        output_height = int(output_width * aspect_ratio / 2)

    # Redimensionar a imagem com melhor qualidade
    img = img.resize((output_width, output_height), Image.LANCZOS)
    
    # Converter para escala de cinza
    img = img.convert('L')
    
    # Converter a imagem para um array numpy
    img_array = np.array(img)
    
    # Normalizar e converter para índices ASCII
    img_normalized = (img_array - img_array.min()) / (img_array.max() - img_array.min())
    img_ascii = np.array([ascii_chars[int(x * (len(ascii_chars) - 1))] for x in img_normalized.flatten()])
    
    # Reformatar para a forma original
    img_ascii = img_ascii.reshape(img_array.shape)
    
    # Converter o array numpy para uma string
    ascii_art = '\n'.join([''.join(row) for row in img_ascii])
    return ascii_art

# Exemplo de uso
image_path = 'face.jpg'

# Carregar a imagem
img = Image.open(image_path)

# Ajustar a largura e a altura para uma resolução melhor
output_width = 150  # Ajuste conforme necessário para a resolução desejada
output_height = None  # Deixe o código calcular a altura

# Converter para ASCII art
ascii_result = image_to_ascii(img, output_width=output_width, output_height=output_height)

# Imprimir a arte ASCII
print(ascii_result)

# Opcionalmente, salvar em um arquivo
with open('ascii_art.txt', 'w') as f:
    f.write(ascii_result)
