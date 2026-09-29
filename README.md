# Help Eletro

Site institucional da Help Eletro, voltado à apresentação de serviços elétricos residenciais, comerciais e industriais.

**Domínio oficial:** [https://helpeletro.com.br](https://helpeletro.com.br)

---

## Sobre o projeto

O site apresenta a empresa, os principais serviços oferecidos, trabalhos realizados, avaliações e formas de contato e orçamento.

O atendimento é direcionado a clientes residenciais, comerciais e industriais em Campinas, Valinhos, Vinhedo, Paulínia, Itatiba e cidades próximas.

A interface é responsiva para desktop, tablet e celular. A publicação é feita pelo GitHub Pages com domínio próprio configurado.

## Principais recursos do site

- Layout responsivo para desktop, tablet e dispositivos móveis
- Header flutuante com navegação por seções
- Menu específico para dispositivos móveis
- Seção de serviços elétricos
- Portfólio de trabalhos realizados
- Lightbox para ampliar as imagens do portfólio
- Seção de avaliações de clientes
- Seção curta de perguntas frequentes
- Formulário de orçamento que monta uma mensagem para o WhatsApp
- Botão flutuante de contato pelo WhatsApp
- Botão de retorno ao topo
- Página de erro 404 personalizada
- Navegação por teclado com foco visível e link para pular ao conteúdo
- Animações suaves de entrada e interação
- Suporte à preferência `prefers-reduced-motion`
- Imagens otimizadas em WebP, com carregamento adiado fora da primeira dobra
- Favicon, ícones para dispositivos e Web App Manifest
- Dados estruturados Schema.org em JSON-LD
- Metadados para SEO local e URL canônica
- Sitemap e regras de rastreamento
- Metadados Open Graph e Twitter Card para compartilhamento
- Google Analytics 4 (`G-REFQPZ3DHW`) carregado somente após o visitante aceitar o aviso de cookies (LGPD)
- Eventos de clique no WhatsApp, Instagram, avaliações do Google e envio do orçamento enviados ao Analytics
- Link "Preferências de cookies" no rodapé para rever a escolha a qualquer momento

## Tecnologias utilizadas

- HTML5
- CSS3
- JavaScript
- GitHub Pages
- Schema.org com JSON-LD

O projeto não utiliza frameworks JavaScript ou bibliotecas externas para a interface.

## Estrutura do projeto

```text
helpeletro/
├── index.html
├── 404.html
├── styles.css
├── script.js
├── sitemap.xml
├── robots.txt
├── site.webmanifest
├── CNAME
├── favicon.ico
├── favicon-16x16.png
├── favicon-32x32.png
├── apple-touch-icon.png
├── android-chrome-192x192.png
├── android-chrome-512x512.png
└── assets/
    ├── logo-help-eletro.png  (usado no Schema.org)
    ├── logo-help-eletro.webp (usado nas páginas)
    └── imagens dos serviços e trabalhos
```

## Últimas atualizações

- Instala o Google Analytics 4 com aviso de cookies: nada é carregado antes do aceite, sinais de anúncios ficam desativados e a recusa apaga os cookies `_ga`
- `976e7a2` — Aumenta o contraste do texto de atribuição das avaliações (WCAG AA), usa o logo em WebP (64 KB → 16 KB) e adiciona `lastmod` ao sitemap
- `41ea79b` — Remove 13 imagens sem uso em `assets/` (versões JPG/WebP substituídas), reduzindo cerca de 2,9 MB do repositório
- `0f321ac` — Evita carregamento vazio no lightbox
- `c860145` — Melhora performance, acessibilidade, FAQ e página 404
- `336482b` — Reforça identidade da Help Eletro para mecanismos de busca
- `bc18cdc` — Corrige favicon e ícones do site
- `b646a5c` — Refina cursores e interações visuais do site
- `fdaf38c` — Adiciona sitemap e robots para SEO
- `1c1c425` — Mantém seta do WhatsApp alinhada ao texto
- `5f38a73` — Prepara eventos para Google Analytics
- `af8bd7f` — Otimiza imagens do site com WebP

## SEO e indexação

O projeto conta com:

- `sitemap.xml` com a URL oficial do site
- `robots.txt` permitindo o rastreamento e referenciando o sitemap
- Dados estruturados Schema.org para `Electrician` e `WebSite`
- Metadados Open Graph e Twitter Card
- URL canônica no domínio oficial
- Favicon e manifesto configurados
- Domínio próprio publicado pelo GitHub Pages

## Google Analytics

- Propriedade GA4 com ID de medição `G-REFQPZ3DHW`, configurado em `script.js` (bloco `ANALYTICS_CONSENTIMENTO`).
- A escolha do visitante fica salva no navegador (`localStorage`, chave `helpCookieConsent`).
- Eventos enviados: `whatsapp_click`, `quote_form_submit`, `instagram_click` e `google_reviews_click`. Os dados digitados no formulário não são enviados, apenas o serviço selecionado.

## Contato

- **Site:** [https://helpeletro.com.br](https://helpeletro.com.br)
- **WhatsApp:** [(19) 99728-7304](https://wa.me/5519997287304)
- **Instagram:** [@help_eletro25](https://www.instagram.com/help_eletro25)
