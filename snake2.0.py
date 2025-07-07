import tkinter
import random

# Configurações do jogo
rows = 25
colunas = 25
tile_size = 25

window_width = colunas * tile_size
window_height = rows * tile_size

# Classe para representar cada bloco
class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Janela do jogo
windown = tkinter.Tk()
windown.title("Snake Game")
windown.resizable(False, False)

canvas = tkinter.Canvas(windown, width=window_width, height=window_height,
                        borderwidth=0, highlightthickness=0, bg="black")
canvas.pack()

# Centralizar a janela na tela
windown.update_idletasks()
screen_width = windown.winfo_screenwidth()
screen_height = windown.winfo_screenheight()
windown_x = (screen_width // 2) - (window_width // 2)
windown_y = (screen_height // 2) - (window_height // 2)
windown.geometry(f"{window_width}x{window_height}+{windown_x}+{windown_y}")

# Inicialização da cobra e comida
snake = [Tile(5 * tile_size, 5 * tile_size)]  # Lista com a cabeça
food = Tile(10 * tile_size, 10 * tile_size)

velocidadex = tile_size
velocidadey = 0

# Função para mudar a direção
def mudar_direcao(event):
    global velocidadex, velocidadey
    if event.keysym == "Up" and velocidadey == 0:
        velocidadex = 0
        velocidadey = -tile_size
    elif event.keysym == "Down" and velocidadey == 0:
        velocidadex = 0
        velocidadey = tile_size
    elif event.keysym == "Left" and velocidadex == 0:
        velocidadex = -tile_size
        velocidadey = 0
    elif event.keysym == "Right" and velocidadex == 0:
        velocidadex = tile_size
        velocidadey = 0

# Função para mover a cobra
def mover_cobra():
    # Cria nova cabeça com base na direção
    head = snake[0]
    new_head = Tile(head.x + velocidadex, head.y + velocidadey)
    snake.insert(0, new_head)

    # Verifica se comeu a comida
    if new_head.x == food.x and new_head.y == food.y:
        gerar_nova_comida()
    else:
        snake.pop()  # Remove o último bloco se não comeu

# Gera uma nova comida em local aleatório
def gerar_nova_comida():
    while True:
        x = random.randint(0, colunas - 1) * tile_size
        y = random.randint(0, rows - 1) * tile_size
        # Garante que a comida não apareça dentro da cobra
        if not any(seg.x == x and seg.y == y for seg in snake):
            food.x = x
            food.y = y
            break

# Função principal de desenho
def draw():
    mover_cobra()
    canvas.delete("all")

    # Desenha a comida
    canvas.create_rectangle(
        food.x, food.y, food.x + tile_size, food.y + tile_size,
        fill="red", outline="black"
    )

    # Desenha cada parte da cobra
    for i, part in enumerate(snake):
        color = "green" if i == 0 else "lightgreen"
        canvas.create_rectangle(
            part.x, part.y, part.x + tile_size, part.y + tile_size,
            fill=color, outline="black"
        )

    windown.after(100, draw)

# Inicia o jogo
windown.bind("<KeyPress>", mudar_direcao)
draw()
windown.mainloop()
