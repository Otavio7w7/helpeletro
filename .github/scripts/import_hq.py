from pathlib import Path
import zipfile, re

root = Path('.')
archive = root / 'assets' / 'helpeletro-imagens-hq.zip'
assets = root / 'assets'
expected = {
    'trabalho-tomada-mesa.jpg': 409653,
    'trabalho-refletor.jpg': 334892,
    'trabalho-antes-depois-tomadas.jpg': 295675,
    'trabalho-tomadas-sala.jpg': 278047,
    'trabalho-nossos-trabalhos.jpg': 260013,
}
if not archive.exists():
    raise SystemExit('ZIP HQ não encontrado em assets/')

with zipfile.ZipFile(archive) as z:
    members = {Path(i.filename).name: i for i in z.infolist() if not i.is_dir()}
    for name, size in expected.items():
        if name not in members:
            raise SystemExit(f'Arquivo ausente no ZIP: {name}')
        data = z.read(members[name])
        if len(data) != size:
            raise SystemExit(f'Tamanho inesperado em {name}: {len(data)} != {size}')
        (assets / name).write_bytes(data)

html_path = root / 'index.html'
html = html_path.read_text(encoding='utf-8')
portfolio = '''<section class="portfolio" id="trabalhos"><div class="wrap"><div class="section-head dark-head reveal"><div><p class="kicker">Trabalhos realizados</p><h2>Alguns resultados em campo.</h2></div><p>Uma seleção de serviços reais da Help Eletro. Clique em qualquer imagem para ampliar e ver os detalhes.</p></div><div class="gallery"><button class="work reveal" data-img="assets/antes-depois.jpeg" data-caption="Antes e depois — acabamento elétrico"><img src="assets/antes-depois.jpeg" alt="Antes e depois de acabamento elétrico" loading="lazy" decoding="async"><span class="work-label">Antes e depois <span>Acabamento e regularização</span></span></button><button class="work reveal" data-img="assets/trabalho-tomada-mesa.jpg" data-caption="Instalação de tomada em mesa de escritório"><img src="assets/trabalho-tomada-mesa.jpg" alt="Instalação de tomada em mesa de escritório" loading="lazy" decoding="async"><span class="work-label">Tomada em mesa de escritório <span>Instalação e acabamento</span></span></button><button class="work reveal" data-img="assets/trabalho-refletor.jpg" data-caption="Instalação de refletor e iluminação"><img src="assets/trabalho-refletor.jpg" alt="Instalação de refletor e iluminação" loading="lazy" decoding="async"><span class="work-label">Refletor e iluminação <span>Instalação em campo</span></span></button><button class="work reveal" data-img="assets/trabalho-antes-depois-tomadas.jpg" data-caption="Antes e depois — instalação de tomadas"><img src="assets/trabalho-antes-depois-tomadas.jpg" alt="Antes e depois da instalação de tomadas" loading="lazy" decoding="async"><span class="work-label">Antes e depois — tomadas <span>Organização e acabamento</span></span></button><button class="work reveal" data-img="assets/trabalho-tomadas-sala.jpg" data-caption="Instalação de tomadas em sala"><img src="assets/trabalho-tomadas-sala.jpg" alt="Instalação de tomadas em sala" loading="lazy" decoding="async"><span class="work-label">Tomadas em sala <span>Instalação elétrica</span></span></button><button class="work reveal" data-img="assets/trabalho-nossos-trabalhos.jpg" data-caption="Serviços realizados pela Help Eletro"><img src="assets/trabalho-nossos-trabalhos.jpg" alt="Serviços realizados pela Help Eletro" loading="lazy" decoding="async"><span class="work-label">Nossos trabalhos <span>Execuções reais da Help Eletro</span></span></button><button class="work reveal" data-img="assets/som-iluminacao.jpeg" data-caption="Infraestrutura elétrica e iluminação"><img src="assets/som-iluminacao.jpeg" alt="Infraestrutura elétrica e iluminação" loading="lazy" decoding="async"><span class="work-label">Infraestrutura e iluminação <span>Execução em campo</span></span></button></div><p class="gallery-note">Imagens reais dos serviços da Help Eletro, preservadas em alta qualidade.</p></div></section>'''
html, count = re.subn(r'<section class="portfolio" id="trabalhos">.*?</section>', portfolio, html, count=1, flags=re.S)
if count != 1:
    raise SystemExit(f'Seção de portfólio não encontrada corretamente: {count}')

marker = '/* MOBILE_AUDIT_HQ_2026 */'
if marker not in html:
    css = r'''
/* MOBILE_AUDIT_HQ_2026 */
.gallery{grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;align-items:start}.work{height:auto;aspect-ratio:4/3;min-width:0}.work img{width:100%;height:100%;object-fit:contain}.work-label{text-shadow:0 2px 12px rgba(0,0,0,.55)}
@media(max-width:980px){.section-head{gap:28px;margin-bottom:38px}.gallery{grid-template-columns:repeat(2,minmax(0,1fr))}.work{aspect-ratio:4/3}.reviews-top{gap:24px}.region-grid{gap:34px}}
@media(max-width:700px){:root{--wrap:min(100% - 24px,1180px)}body{overflow-x:hidden}.wrap{min-width:0}header#siteHeader{width:calc(100% - 24px);top:8px;padding:10px 12px;border-radius:16px}header#siteHeader .brand img,header#siteHeader.scrolled .brand img{width:122px;max-height:48px}.mobile{width:44px;height:44px;flex:0 0 44px}.mobile-menu{right:0;top:calc(100% + 8px);width:min(320px,calc(100vw - 24px));max-height:calc(100vh - 92px);overflow-y:auto}.mobile-menu a{min-height:48px}.hero{min-height:660px}.hero-inner{padding:122px 0 72px}.hero-copy{font-size:1rem}.trust{gap:10px 14px}.section-head{display:block;margin-bottom:30px}.section-head>p{margin-top:14px}.about,.diffs,.services,.portfolio,.reviews,.region{padding:70px 0}.about-grid{gap:30px}.about-photo{min-height:340px}.stats{grid-template-columns:1fr}.diff-grid,.cards,.reviews-grid,.gallery{grid-template-columns:1fr}.card-img{height:220px}.card-body{padding:21px}.other{padding:18px;gap:8px}.other strong{width:100%;margin:0 0 4px}.work{height:auto;min-height:0;aspect-ratio:auto;border-radius:18px}.work img{height:auto;max-height:none;object-fit:contain}.work-label{left:14px;right:14px;bottom:13px;font-size:.94rem}.work-label span{font-size:.76rem}.gallery{gap:14px}.gallery-note{margin-top:14px}.reviews-top{display:block;margin-bottom:24px}.google-score{gap:9px 12px}.google-score strong{font-size:2.6rem}.stars{font-size:1.15rem}.reviews-actions{margin-top:18px;width:100%}.reviews-actions .google-btn{width:100%;flex:none}.review-card{padding:19px}.region-grid{gap:28px}.cities p{padding:15px 4px}.cta{padding:58px 0}.cta-inner{gap:24px}.cta-inner .btn{width:100%}.footer-grid{gap:30px;padding-bottom:36px}.footer-bottom{gap:6px}.wa{right:14px;bottom:14px;width:56px;height:56px}.top{right:14px;bottom:80px}.lightbox{padding:10px}.lightbox-card{width:100%}.lightbox img{max-height:80vh;border-radius:14px}.close{top:8px;right:8px;z-index:2}.caption{padding:0 4px;font-size:.9rem}}
@media(max-width:380px){h1{font-size:2.45rem}.hero-inner{padding-top:116px}.trust{font-size:.82rem}.google-score strong{font-size:2.35rem}.review-card{padding:17px}.other span{font-size:.78rem}.footer-grid{gap:26px}}
'''
    html = html.replace('</style>', css + '\n</style>', 1)

html_path.write_text(html, encoding='utf-8')
archive.unlink()
for name, size in expected.items():
    actual = (assets / name).stat().st_size
    print(f'{name}: {actual} bytes')
    if actual != size:
        raise SystemExit(f'Falha de integridade em {name}')
