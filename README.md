<details>
<summary>PT-BR</summary>
<details>
<summary>Descrição</summary>

# Case Técnico — Fullstack (Vue 3 + Django)
## Objetivo
Desenvolver uma aplicação completa para gerenciamento e listagem de itens (ex: Eventos,
Produtos, Projetos ou Imóveis — o domínio do negócio fica a sua escolha).
O foco principal é avaliar suas decisões de arquitetura, modelagem de
dados, integração entre camadas e a qualidade da implementação (Clean Code,
componentização e performance).
Nota: Não existe “bala de prata”. Esperamos que você escolha as ferramentas/padrões
e justifique suas escolhas no README.
## Stack Tecnológica Obrigatória
### Backend
Python + Django
Framework de API: Django REST Framework (DRF) ou Django Ninja (sua
escolha).
Banco de Dados: SQLite (aceitável) ou PostgreSQL (diferencial via Docker).
### Frontend
Vue 3 + Vite (Composition API obrigatória).
Framework CSS: Escolha um entre TailwindCSS, UnoCSS, Vuetify ou Quasar.
## Requisitos do Desafio
Você tem liberdade para definir a estrutura de pastas (Monorepo ou repositórios separados)
e a organização do código.
1. Backend (API &amp; Dados)
Deve prover endpoints para suportar o frontend, garantindo performance e integridade.
Modelagem: Criar modelos que representem o item escolhido (deve ter id, título,
descrição, imagem/url, data e status).
Paginação: Implementar paginação no servidor.
Filtros e Busca: Endpoint de listagem deve aceitar parâmetros de busca textual e
ordenação.
Favoritos (Persistência): A funcionalidade de “favoritar” deve ser salva no banco
de dados (relação User &lt;-&gt; Item ou via LocalStorage sincronizado, justifique sua
abordagem).
Delay Simulado (Opcional): Se rodar localmente for “rápido demais”, adicione um
pequeno sleep nas views para provar que seus loadings e skeletons no front
funcionam.
2. Frontend (UI &amp; UX)
A interface deve ser responsiva e resiliente.
Scroll Infinito Manual: Implementar a lógica de carregar mais itens ao chegar no
fim da lista.

Busca: Input de busca que consulta a API. A busca deve resetar a lista atual e a
paginação.
Roteamento (Vue Router):
/: Listagem infinita (estado da busca/filtros deve refletir na URL).
/items/:id Detalhe do item (carregado via API).
/favoritos: Listagem dos itens favoritados.
 Componentização: Crie componentes reutilizáveis (ex: Card, Button, Input, Loader).
 Estados de UI: Tratamento visual para: Carregando (Skeletons), Erro (com botão de
retry), Lista Vazia e Fim dos Resultados.
3. Arquitetura e Decisões (O “Pulo do Gato”)
Como este é um teste fullstack aberto, queremos ver como você pensa:
Tomada de Decisão: Não se atenha somente aos requisitos escritos, busque
implementar pequenas funcionalidades que estão relacionadas aos requisitos.
Tailwind/UnoCSS vs Quasar/Vuetify: Por que escolheu um ou outro?
(Produtividade? Performance? Bundle size?).
Estratégia de API: Serializers complexos ou Schemas simples?
Otimização: Como você lida com o problema de N+1 no Django? Como evita re-
renderizações desnecessárias no Vue?
Restrições Técnicas
1. Frontend - Sem Atalhos de Scroll: Não utilize bibliotecas prontas de infinite scroll
(ex: vue-infinite-loading). Crie seu próprio composable ou diretiva.
2. Frontend - Fetching Manual: Não utilize libs de data fetching reativo (como
TanStack Query ou SWR) neste teste. O objetivo é avaliar sua capacidade de
criar Composables próprios (ex: useFetch, useInfiniteList) gerenciando estados de
loading, error e data manualmente com Axios.
3. Commits Semânticos: O histórico do git deve contar a história da construção (ex:
feat: setup django models, style: implement cards with tailwind).
4. Linting: O projeto deve ter ESLint/Prettier (Front) e Flake8/Black/Ruff (Back)
configurados.
## Diferenciais (Opcionais)
Se quiser ir além e demonstrar seniority:
Docker / Docker Compose: Um comando (docker-compose up) para subir banco,
back e front.
TypeScript: Tipagem forte no Vue e Type Hints no Python.
Testes:
Backend: Pytest cobrindo ao menos o endpoint de listagem.

Frontend: Vitest testando a lógica de um Composable ou Componente.
Performance: Uso de select_related/prefetch_related no Django para otimizar
queries.
Dark Mode: Implementação manual ou via framework escolhido, com persistência.
## Entregáveis
1. Link do Repositório (GitHub/GitLab): Público.
2. README.md (Crucial):
### Instruções claras de como rodar (Back + Front).
### Justificativa das Decisões:
Por que escolheu essa estrutura de pastas?
Por que escolheu a Framework CSS?
Qual foi a estratégia de paginação e cache?
Prints ou GIFs da aplicação rodando.
O que você melhoraria se tivesse mais tempo? (Dívidas técnicas assumidas).
</details>
<details>
<summary>Respostas</summary>

# Respostas:
## Por que escolheu Django REST Framework?

R: Por causa da familiaridade e por já trabalhar com ele há um tempo, como sendo um teste e o tempo sendo curto, essa foi a escolha por mais que o a curva de aprendizagem do Django Ninja seja baixa. Também pelo fato do Django REST Framework já prover autenticação, filtros e permissões.

## Por que escolheu Vuetify?

R: Por conta da produtividade que ele oferece apesar do bundle maior do que Tailwind e UnoCSS, e também por não ter um design próprio definido, caso houvesse uma das opções seria o Tailwind pelo fato da liberdade de criar components com UI bem customizadas pela liberdade que ele oferece.

## Qual foi a estratégia de paginação e cache?

R: A estrategia de paginação foi a default do Django, como ele já oferece esse tipo de feature, usei a padrão. Já o cache, não foi feito, mas se fosse feito seria via Redis principalmente para contagem de produtos e produtos favoritados invalidando quando alterados, em dados que não são muito voláteis. Cache no NGINX também seria uma opção.

## Qual a estratégia feita para evitar disparo de múltiplos requests na pesquisa:

R: Uso de debounce em TextFields com alguns segundos de delay para evitar requests a cada caracter digitado.

## Por que escolheu essa estrutura de pastas?

R: Porque por mais extenso que possa ficar, os arquivos ficam melhores organizados e os paths fica mais claros para cada tipo de modulo que está sendo importado.

## Por que utilizou Docker Compose:

R: Porque é um ótimo método para subir aplicações sem restrições e erros em ambientes e sistemas operacionais diferentes, garantindo o funcionamento da aplicação em qualquer ambiente/SO. Sem o famoso no meu PC funciona.

## Como você lida com o problema de N+1 no Django?
R: Uso de select_related para relações um pra um (ForeignKey e OneToOne) e prefetch_related para muitos para muitos (ManyToMany), limitação de colunas no select. E para identificação desse problema pode ser usado Django Silk que é uma profilling e ferramenta de inspeção que pode mostrar comportamentos que acontecem quando está com o problema de N+1.

## Como evita re-renderizações desnecessárias no Vue?
R: Evitar usos de objetos reativos muito aninhados, utilzação de computed ao invês de funções para tratar dados, dividir componentes muito grandes (componentização) e uso cuidadoso do watch evitando deep watchers e utilizando somente objetos reativos que são convenientes para aquele watch.

## O que você melhoraria se tivesse mais tempo? (Dívidas técnicas assumidas):

R: Primeiramente terminaria 100% o teste, implementando os detalhes que faltaram e a parte de favoritar.
Começaria pelo Django Ninja, por ser mais simples dado o tamanho do teste, usaria Tailwind para ter um menor bundle no frontend.
Terminaria o sistema de favoritar como mencionando utilizando relação many to many no banco de dados, guardando em cache no backend invalidando sempre que um novo produto fosse favoritado evitando requests para o frontend pelo motivo de ser a melhor abordagem para persistir dados em multiplos dispositivos, sendo que o local storage somente seria guardado no dispositivo e browser que o usuario estiver usando.
</details>
</details>

<details>
<summary>EN</summary>
<details>
<summary>Description</summary>

# Technical Case — Fullstack (Vue 3 + Django)
## Objective

Develop a complete application for managing and listing items (e.g. Events,
Products, Projects, or Real Estate — the business domain is up to you).
The main focus is to evaluate your architecture decisions, data modeling,
layer integration, and the quality of the implementation
(Clean Code, componentization, and performance).

Note: There is no “silver bullet.” We expect you to choose the tools/patterns
and justify your choices in the README.

## Mandatory Technology Stack
### Backend
Python + Django
API Framework: Django REST Framework (DRF) or Django Ninja (your choice)
Database: SQLite (acceptable) or PostgreSQL (a plus via Docker)

### Frontend
Vue 3 + Vite (Composition API is mandatory)
CSS Framework: Choose one among TailwindCSS, UnoCSS, Vuetify, or Quasar
## Challenge Requirements
You are free to define the folder structure (Monorepo or separate repositories)
and code organization.

1. Backend (API & Data)
Must provide endpoints to support the frontend, ensuring performance and integrity.
Modeling: Create models representing the chosen item (must include id, title,
description, image/url, date, and status).
Pagination: Implement server-side pagination.
Filters and Search: The listing endpoint must accept textual search and
ordering parameters.
Favorites (Persistence): The “favorite” functionality must be persisted in
the database (User ↔ Item relationship or synchronized LocalStorage — justify
your approach).
Simulated Delay (Optional): If running locally is “too fast,” add a small
sleep in the views to prove that frontend loadings and skeletons work.

2. Frontend (UI & UX)
The interface must be responsive and resilient.
Manual Infinite Scroll: Implement logic to load more items when reaching the
end of the list.
Search: Search input that queries the API. Searching must reset the current
list and pagination.
Routing (Vue Router)
/ — Infinite listing (search/filter state must be reflected in the URL)
/items/:id — Item detail (loaded via API)
/favorites — List of favorited items
Componentization: Create reusable components (e.g. Card, Button, Input, Loader).
UI States: Visual handling for: Loading (Skeletons), Error (with retry button),
Empty List, and End of Results.

3. Architecture and Decisions (The “Trick”)
As this is an open fullstack test, we want to see how you think:
Decision Making: Don’t stick only to the written requirements; try to implement
small features related to them.
Tailwind/UnoCSS vs Quasar/Vuetify: Why did you choose one over the other?
(Productivity? Performance? Bundle size?)
API Strategy: Complex serializers or simple schemas?
Optimization: How do you handle the N+1 problem in Django? How do you avoid
unnecessary re-renders in Vue?
## Technical Constraints
Frontend — No Scroll Shortcuts: Do not use ready-made infinite scroll
libraries (e.g. vue-infinite-loading). Create your own composable or directive.
Frontend — Manual Fetching: Do not use reactive data fetching libraries
(such as TanStack Query or SWR). The goal is to evaluate your ability to create
your own Composables (e.g. useFetch, useInfiniteList) managing loading, error,
and data states manually with Axios.
Semantic Commits: Git history must tell the story of the build
(e.g. feat: setup django models, style: implement cards with tailwind).
Linting: The project must have ESLint/Prettier (Front) and
Flake8/Black/Ruff (Back) configured.

## Differentials (Optional)

If you want to go further and demonstrate seniority:

Docker / Docker Compose: One command (docker-compose up) to start database,
backend, and frontend.
TypeScript: Strong typing in Vue and type hints in Python.
Tests:
Backend: Pytest covering at least the listing endpoint.
Frontend: Vitest testing the logic of a Composable or Component.
Performance: Use of select_related / prefetch_related in Django to optimize queries.
Dark Mode: Manual implementation or via the chosen framework, with persistence.

## Deliverables

Repository Link (GitHub/GitLab): Public.
README.md (Crucial):
Clear instructions on how to run (Back + Front).
Decision Justification:
Why did you choose this folder structure?
Why did you choose this CSS framework?
What was the pagination and cache strategy?
Screenshots or GIFs of the application running.
What would you improve if you had more time? (Assumed technical debt).
</details>
<details>
<summary>Answers</summary>
  
# Answers

## Why did you choose Django REST Framework?

A: Because of familiarity and having worked with it for some time. Since this is a test
and time is limited, this was the safest choice, even though Django Ninja has a low
learning curve. Also because Django REST Framework already provides authentication,
filters, and permissions.

## Why did you choose Vuetify?

A: Due to the productivity it offers, despite having a larger bundle than Tailwind
and UnoCSS. Also because it does not enforce a strict design system. If a custom UI
were required, Tailwind would be the choice due to the freedom it provides to build
highly customized components.

## What was the pagination and cache strategy?

A: The pagination strategy used was Django’s default pagination, since it already
provides this feature out of the box. Cache was not implemented, but if it were,
Redis would be used mainly for product counts and favorited products, invalidating
the cache whenever changes occur, especially for less volatile data. NGINX caching
would also be an option.

## What strategy was used to avoid multiple requests during search?

A: Use of debounce on TextFields with a few seconds of delay to avoid requests on
every typed character.

## Why did you choose this folder structure?

A: Because even though it can become extensive, files remain better organized and
paths become clearer for each type of imported module.

## Why did you use Docker Compose?

A: Because it is an excellent way to run applications without environment or OS
restrictions, ensuring the application works anywhere. Avoiding the classic
“it works on my machine” problem.

## How do you deal with the N+1 problem in Django?

A: By using select_related for one-to-one relationships (ForeignKey and OneToOne) and prefetch_related for many-to-many relationships (ManyToMany), as well as limiting selected columns in queries. To identify this issue, tools like Django Silk can be used, which is a profiling and inspection tool that helps visualize query behavior and detect N+1 problems.

## How do you avoid unnecessary re-renders in Vue?

A: By avoiding deeply nested reactive objects, using computed properties instead of functions to process data, splitting very large components into smaller ones (componentization), and carefully using watch, avoiding deep watchers and only observing reactive objects that are truly relevant for that watcher.

## What would you improve if you had more time? (Assumed technical debt)

A: First, I would fully complete the test, implementing the missing details and the
favorites feature.
I would start using Django Ninja, as it is simpler given the test size, and use
Tailwind to achieve a smaller frontend bundle.
I would complete the favorites system using a many-to-many relationship in the
database, caching it on the backend and invalidating it whenever a new product is
favorited, avoiding unnecessary frontend requests. This is the best approach for
persisting data across multiple devices, since LocalStorage only persists data on
the specific device and browser used by the user.
</details>
</details>
