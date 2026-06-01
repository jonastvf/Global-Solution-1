# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="assets/logo-fiap.png" 
       alt="FIAP - Faculdade de Informática e Administração Paulista" 
       width="40%">
</a>
</p>

<br>

# AstroDash - Monitoramento de Clima Espacial e Riscos Orbitais 🚀

## Nome do grupo

### Grupo São Paulo e Interior

## Integrantes

- <a href="https://www.linkedin.com/in/jonastadeufernandes">Jonas Tadeu V. Fernandes - RM563027</a>
- <a href="https://www.linkedin.com/">Levi Passos Silveira Marques - RM56557</a>
- <a href="https://www.linkedin.com/in/raphaelsilva-phael">Raphael da Silva - RM561452</a>
- <a href="https://www.linkedin.com/in/raphael-dinelli-8a01b278">Raphael Dinelli Neto - RM562892</a>
- <a href="https://www.linkedin.com/in/yan-cotta">Yan Pimental Cotta - RM562836</a>

## Professores

### Tutor

- <a href="https://www.linkedin.com/in/caique-nonato/">Caique Nonato da Silva Bezerra</a>

### Coordenador

- <a href="https://www.linkedin.com/in/andregodoichiovato">André Godoi</a>

## 🎯 A Proposta: A Nova Economia Espacial
A economia global atual depende criticamente da infraestrutura em órbita (satélites de telecomunicação, GPS, monitoramento climático). No entanto, o clima espacial — como tempestades solares e aproximação de asteroides (NEOs) — representa um risco constante de bilhões de dólares para esses equipamentos. 

O **AstroDash** é uma Prova de Conceito (POC) de um dashboard inteligente que democratiza o acesso a esses dados críticos. Ele consome dados oficiais em tempo real e utiliza Inteligência Artificial Generativa para traduzir métricas técnicas complexas em relatórios de risco claros e acionáveis.

## ⚙️ Arquitetura e Tecnologias Utilizadas
A solução foi arquitetada focando em eficiência, escalabilidade e integração de APIs, cumprindo os requisitos da disciplina:

* **Linguagem Principal:** Python 
* **Front-end / Dashboard:** Streamlit (Criação de interface web interativa e visualização de dados).
* **Coleta de Dados:** Requisições automatizadas para a API pública da NASA (NeoWs / DONKI).
* **Inteligência Artificial:** Integração com API de IA Generativa ([Inserir se usaram Gemini ou OpenAI]) para processamento de linguagem natural e análise de risco automatizada.

### Como a solução atende aos requisitos mínimos da GS:
1. **Uso de APIs e Dashboards:** Os dados são extraídos via API da NASA e plotados dinamicamente na interface Streamlit.
2. **Aplicação de IA Generativa:** Um módulo da aplicação envia o JSON de dados espaciais brutos para um LLM (Large Language Model), solicitando um resumo executivo sobre os riscos de impacto ou interferência eletromagnética no dia atual.
3. *Nota sobre Hardware:* Conforme edital, a integração com IoT/Edge Computing foi dispensada por não ser aplicável ao escopo de um software de monitoramento via dados em nuvem.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>docs</b>: Pasta destinada à documentação textual, incluindo brainstorm, atas e registros de reuniões, desenhos, prints, diagramas, storyboard, estratégia de IA e arquitetura e etc.

- <b>src</b>: Todo o código fonte desenvolvido, como scripts em Python, R, JS ou HTML, notebooks, códigos para ESP32/Arduino, APIs ou microsserviços, além de modelos, inferências e etc. Os tipos de arquivos e códigos são definidos no enunciado da atividade.

- <b>data</b>: Contém os dados utilizados, como arquivos CSV, Excel, JSON, bases sintéticas e etc.

- <b>README.md</b>: Arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 📎 Links e Observações

- <b>Listagem de Links</b>: Links do projeto (ex. vídeos da entrega, páginas, etc.), 

- <b>Explicação de decisões técnicas</b>: Observações do projeto,

- <b>Observações Gerais</b>: Caso o projeto seja relacionado à alguma competição, deixar registrado no README se aceita ou não participar.


## 🔧 Como executar o código

### Pré-requisitos
* Python 3.8+ instalado.
* Chave de API da NASA (obtida gratuitamente em api.nasa.gov).
* Chave de API da [Gemini/OpenAI].



## 🗃 Histórico de lançamentos

* 0.5.0 - XX/XX/2024
    * 
* 0.4.0 - XX/XX/2024
    * 
* 0.3.0 - XX/XX/2024
    * 
* 0.2.0 - XX/XX/2024
    * 
* 0.1.0 - XX/XX/2024
    *

---


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
