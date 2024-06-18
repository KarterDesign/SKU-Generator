
# SKU Generator 3000

## Visão Geral

Este projeto é um gerador de SKU (Stock Keeping Unit) desenvolvido em Python usando a biblioteca Gradio para criar uma interface de usuário simples e interativa. O objetivo do projeto é facilitar a criação de SKUs para diferentes tipos de produtos e eventos, baseando-se em parâmetros específicos fornecidos pelo usuário.

## Estrutura do Projeto

O projeto é composto por um único arquivo Python: `SKU Generator 3000.py`.

### Dependências

As dependências principais para este projeto são:

-   Gradio: Para criar a interface web interativa.

Você pode instalar as dependências necessárias utilizando o seguinte comando:

bash

Copiar código

`pip install gradio` 

### Código Principal

O código principal do projeto é organizado da seguinte forma:

1.  **Importação da biblioteca Gradio:**
    
    python
    
    Copiar código
    
    `import gradio as gr` 
    
2.  **Definição da função `gerar_sku` que cria o SKU baseado nos parâmetros fornecidos:**
    
    python
    
    Copiar código
    
    `def gerar_sku(pais, ano, evento, abreviacao_evento, tipo, produto):
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
        return sku` 
    
3.  **Definição da interface Gradio:**
    
    python
    
    Copiar código
    
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
    

### Como Executar

Para executar o projeto, siga os seguintes passos:

1.  Certifique-se de que todas as dependências estão instaladas.
    
2.  Execute o arquivo `SKU Generator 3000.py` usando o comando:
    
    bash
    
    Copiar código
    
    `python SKU\ Generator\ 3000.py` 
    
3.  A interface Gradio será aberta no seu navegador padrão, onde você poderá inserir os parâmetros necessários para gerar o SKU.
    

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias, correções de bugs ou novas funcionalidades.

## Licença

Este projeto está licenciado sob a MIT License.

## Contato

Para mais informações, entre em contato com seu-email@dominio.com.
