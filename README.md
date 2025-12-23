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
Por que escolheu Django REST Framework?
R: Por causa da familiaridade e por já trabalhar com ele há um tempo, como sendo um teste e o tempo sendo curto, essa foi a escolha por mais que o a curva de aprendizagem do Django Ninja seja baixa. Também pelo fato do Django REST Framework já prover autenticação, filtros e permissões.
Por que escolheu Vuetify?
R: Por conta da produtividade que ele oferece apesar do bundle maior do que Tailwind e UnoCSS, e também por não ter um design próprio definido, caso houvesse uma das opções seria o Tailwind pelo fato da liberdade de criar components com UI bem customizadas pela liberdade que ele oferece.
Qual foi a estratégia de paginação e cache?
R: A estrategia de paginação foi a default do Django, como ele já oferece esse tipo de feature, usei a padrão. Já o cache, não foi feito, mas se fosse feito seria via Redis principalmente para contagem de produtos e produtos favoritados invalidando quando alterados, em dados que não são muito voláteis. Cache no NGINX também seria uma opção.
Qual a estratégia feita para evitar disparo de múltiplos requests na pesquisa:
R: Uso de debounce em TextFields com alguns segundos de delay para evitar requests a cada caracter digitado.
Por que escolheu essa estrutura de pastas?
R: Porque por mais extenso que possa ficar, os arquivos ficam melhores organizados e os paths fica mais claros para cada tipo de modulo que está sendo importado.
Por que utilizou Docker Compose:
R: Porque é um ótimo método para subir aplicações sem restrições e erros em ambientes e sistemas operacionais diferentes, garantindo o funcionamento da aplicação em qualquer ambiente/SO. Sem o famoso no meu PC funciona.

O que você melhoraria se tivesse mais tempo? (Dívidas técnicas assumidas):
R: Primeiramente terminaria 100% o teste, implementando os detalhes que faltaram e a parte de favoritar.
Começaria pelo Django Ninja, por ser mais simples dado o tamanho do teste, usaria Tailwind para usar um menor bundle no frontend.
Terminaria o sistema de favoritar como mencionando utilizando relação many to many no banco de dados, guardando em cache no backend invalidando sempre que um novo produto fosse favoritado evitando requests para o frontend.
<details>
</details>
