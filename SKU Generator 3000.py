import gradio as gr

def gerar_sku(pais, ano, evento, abreviacao_evento, tipo, produto):
    # Formata o ano para pegar apenas os últimos dois dígitos
    ano_formatado = str(ano)[-2:]

    # Abreviação do tipo
    tipos = {
        "Evento": "EVT",
        "Ingresso": "ING",
        "Hotel": "HTL",
        "Quarto": "QRT"
    }
    abreviacao_tipo = tipos[tipo]

    # Monta o SKU
    sku = f"{pais}{ano_formatado}{abreviacao_evento.upper()}{abreviacao_tipo}{produto.replace(' ', '').upper()}"
    return sku

# Define a interface Gradio
iface = gr.Interface(
    fn=gerar_sku,
    inputs=[
        gr.Dropdown(choices=["BR", "US", "DE"], label="País"),
        gr.Textbox(label="Ano", placeholder="Digite o ano"),
        gr.Textbox(label="Evento", placeholder="Nome do evento"),
        gr.Textbox(label="Abreviação desejada", placeholder="Abreviação do evento"),
        gr.Dropdown(choices=["Evento", "Ingresso", "Hotel", "Quarto"], label="Tipo"),
        gr.Textbox(label="Produto", placeholder="Digite o nome do produto")
    ],
    outputs=gr.Textbox(),
    title="Gerador de SKU"
)

iface.launch()
