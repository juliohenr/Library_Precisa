import requests

## Fantasy

request = '{"book_name": "Harry Potter e a ordem da Fênix", "author": "J . K Rolling", "volume": 1, "version": 2, "category": "Fantasia","synopsis": "Harry não é mais um garoto. Aos 15 anos, continua sofrendo a rejeição dos Dursdley, sua estranha família no mundo dos trouxas. Também continua contando com Rony Weasley e Hermione Granger, seus melhores amigos em Hogwarts, para levar adiante suas investigações e aventuras. Mas o bruxinho começa a sentir e descobrir coisas novas, como o primeiro amor e a sexualidade. Nos volumes anteriores, J. K. Rowling mostrou como Harry foi transformado em celebridade no mundo da magia por ter derrotado, ainda bebê, Voldemort, o todo-poderoso bruxo das trevas que assassinou seus pais. Neste quinto livro da saga, o protagonista, numa crise típica da adolescência, tem ataques de mau humor com a perseguição da imprensa, que o segue por todos os lugares e chega a inventar declarações que nunca deu. Harry vai enfrentar as investidas de Voldemort sem a proteção de Dumbledore, já que o diretor de Hogwarts é afastado da escola. E vai ser sem a ajuda de seu protetor que o jovem herói enfrentará descobertas sobre a personalidade controversa de seu pai, Tiago Potter, e a morte de alguém muito próximo."}'

files =  {'file': open('images/Harry Potter e a ordem da Fênix.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))



request = '{"book_name": "Senhor dos Anéis Sociedade do Anel", "author": "J . R . R TOLKIEN", "volume": 1, "version": 1, "category": "Fantasia","synopsis": "Numa terra fantástica e única, chamada Terra-Média, um hobbit (seres de estatura entre 80 cm e 1,20 m, com pés peludos e bochechas um pouco avermelhadas) recebe de presente de seu tio o Um Anel, um anel mágico e maligno que precisa ser destruído antes que caia nas mãos do mal. Para isso o hobbit Frodo (Elijah Woods) terá um caminho árduo pela frente, onde encontrará perigo, medo e personagens bizarros. Ao seu lado para o cumprimento desta jornada aos poucos ele poderá contar com outros hobbits, um elfo, um anão, dois humanos e um mago, totalizando 9 pessoas que formarão a Sociedade do Anel."}'

files =  {'file': open('images/senhor_dos_aneis.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))



request = '{"book_name": "Herança", "author": "Christopher Paolini", "volume": 1, "version": 1, "category": "Fantasia","synopsis": "Herança é o quarto e último livro da série Ciclo da Herança, do escritor norte-americano Christopher Paolini. A história acompanha a vida de Eragon, um Cavaleiro de Dragões do continente ficcional de Alagaësia, que luta junto de seu dragão Saphira para acabar com o reinado opressor do Imperador Galbatorix."}'

files =  {'file': open('images/eragon_heranca.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))



request = '{"book_name": "As Crônicas de Gelo e Fogo", "author": "George R.R. Martin", "volume": 1, "version": 1, "category": "Fantasia","synopsis": "Quando Eddard Stark, lorde do castelo de Winterfell, aceita a prestigiada posição de Mão do Rei oferecida pelo velho amigo, o rei Robert Baratheon, não desconfia que sua vida está prestes a ruir em sucessivas tragédias."}'

files =  {'file': open('images/cronicas_de_gelo_e_fogo.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "Excalibur", "author": "Bernard Cornwell", "volume": 1, "version": 1, "category": "Fantasia","synopsis": "Durante a era medieval, o rei Uther Pendragon recebe do mago Merlin a mística espada Excalibur. ... Com a Inglaterra dividida pela ausência de um rei, vários nobres disputam a posse da espada, mas apenas o jovem Arthur, filho de Uther, auxiliado por Merlin, consegue retirá-la."}'

files =  {'file': open('images/excalibur.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "O Hobbit", "author": "J . R . R TOLKIEN", "volume": 1, "version": 1, "category": "Fantasia","synopsis": "O Hobbit conta a história de Bilbo Bolseiro, um Hobbit pacato e satisfeito cuja vida vira de cabeça para baixo quando ele se junta ao mago Gandalf e a treze anões em sua jornada para reaver um tesouro roubado."}'

files =  {'file': open('images/hobbit.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))



request = '{"book_name": "Crepúsculo", "author": "Stephenie Meyer", "volume": 1, "version": 1, "category": "Fantasia","synopsis": "Crepúsculo poderia ser uma história comum, não fosse um elemento irresistível: o objeto da paixão da protagonista é um vampiro. Assim, soma-se à paixão um perigo sobrenatural temperado com muito suspense"}'

files =  {'file': open('images/crepusculo.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

## Suspense


request = '{"book_name": "Garota Exemplar", "author": "Gillian Flynn", "volume": 1, "version": 1, "category": "Suspense","synopsis": "Desde sua publicação, em 2012, Garota exemplar tornou-se sucesso de público e crítica, alcançando o topo das mais prestigiadas listas de mais vendidos ao redor do mundo e consagrando sua autora, Gillian Flynn, como a mais aclamada escritora de suspense da atualidade. Agora, a trama sobre o casamento que sai tragicamente dos eixos chega aos cinemas, numa superprodução da Twentieth Century Fox dirigida por David Fincher (A rede social e Clube da luta) e estrelada por Ben Affleck e Rosamund Pike. O roteiro é assinado pela própria Gillian Flynn."}'

files =  {'file': open('images/garota-exemplar.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "Caixa de Pássaros", "author": "Josh Malerman", "volume": 1, "version": 1, "category": "Suspense","synopsis": "Romance de estreia de Josh Malerman, Caixa de pássaros é um thriller psicológico tenso e aterrorizante, que explora a essência do medo. Uma história que vai deixar o leitor completamente sem fôlego mesmo depois de terminar de ler.Basta uma olhadela para desencadear um impulso violento e incontrolável que acabará em suicídio. Ninguém é imune e ninguém sabe o que provoca essa reação nas pessoas. Cinco anos depois do surto ter começado, restaram poucos sobreviventes, entre eles Malorie e dois filhos pequenos. Ela sonha em fugir para um local onde a família possa ficar em segurança, mas a viagem que tem pela frente é assustadora: uma decisão errada e eles morrerão.“Malerman usa a narrativa alusiva para criar um thriller fascinante que os fãs de Stephen King vão adorar.”Publishers Weekly“Deve ser lido de uma só vez. Ninguém ainda havia escrito uma história de terror como essa.”Hugh Howey, autor de SiloBest seller VEJA"}'

files =  {'file': open('images/caixa-de-passaros.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "O Silêncio dos Inocentes", "author": "Thomas Harris", "volume": 1, "version": 1, "category": "Suspense","synopsis": "Livro que deu origem ao filme com Anthony Hopkins e Jodie Foster. Cinco mulheres são brutalmente assassinadas em diferentes localidades dos Estados Unidos. Para chegar até o sanguinário assassino, a jovem agente do FBI, Clarice Starling, entrevista o ardiloso psiquiatra Hannibal Lecter, cuja mente psicopata está perigosamente voltada para o crime. Ao seguir as pistas apontadas por Dr. Lecter, Clarice se envolve em uma teia mortífera surpreendente, narrada no texto arrepiante de Thomas Harris. Em 1991, a adaptação para o cinema de O silêncio dos inocentes rendeu ao filme cinco estatuetas do Oscar."}'

files =  {'file': open('images/o-silencio-dos-inocentes.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "Assassinato no Expresso Oriente", "author": "Agatha Christie", "volume": 1, "version": 1, "category": "Suspense","synopsis": "Em meio a uma viagem, Hercule Poirot é surpreendido por um telegrama solicitando seu retorno a Londres. Então, o famoso detetive belga embarca no Expresso do Oriente, que está inesperadamente cheio para aquela época do ano. Pouco tempo após a meia-noite, o excesso de neve nos trilhos obriga o trem a parar. Na manhã seguinte, o corpo de um dos passageiros é encontrado, golpeado por múltiplas facadas. Com os passageiros isolados por conta da neve, e tendo um assassino entre eles, a única solução é que Poirot inicie uma investigação para descobrir quem é o criminoso ― antes que se faça mais uma vítima."}'

files =  {'file': open('images/assassinato-oriente.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

request = '{"book_name": "O Iluminado", "author": "Stephen King", "volume": 1, "version": 1, "category": "Suspense","synopsis": "O lugar perfeito para recomeçar”, é o que pensa Jack Torrance ao ser contratado como zelador para o inverno. Hora de deixar para trás o alcoolismo, os acessos de fúria, os repetidos fracassos. Isolado pela neve com a esposa e o filho, tudo o que Jack deseja é um pouco de paz para se dedicar à escrita. Mas, conforme o inverno se aprofunda, o local paradisíaco começa a parecer cada vez mais remoto... e mais sinistro. Forças malignas habitam o Overlook, e tentam se apoderar de Danny Torrance, um garotinho com grandes poderes sobrenaturais. Possuir o menino, no entanto, se mostra mais difícil do que esperado. Então os espíritos resolvem se aproveitar das fraquezas do pai... Um dos livros mais assustadores de todos os tempos, O iluminado é um clássico de Stephen King. Edição especial com tradução revisada e prólogo e epílogo inéditos."}'

files =  {'file': open('images/o-iluminado.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

request = '{"book_name": "Você", "author": "Caroline Kepnes", "volume": 1, "version": 1, "category": "Suspense","synopsis": "Livro que inspirou a série original da Netflix. Quando uma aspirante a escritora linda e atraente entra na livraria do East Village onde Joe Goldberg trabalha, ele faz o que (quase) qualquer pessoa interessada faria: pesquisa no Google o nome que consta em seu cartão de crédito. Para a sorte de Joe, existe apenas uma Guinevere Beck na cidade de Nova York, e ela posta incessantemente nas redes sociais tudo o que ele precisa saber: que ela é apenas Beck para os amigos, que frequentou a Brown University, mora na Bank Street e estará em um bar no Brooklyn esta noite - o lugar perfeito para um encontro ao acaso. Ela ainda não sabe, mas é a mulher perfeita para Joe. E quando Joe começa a orquestrar obsessivamente uma série de eventos para garantir que Beck caia em seus braços, ela acaba não resistindo às suas investidas. Passando do papel de stalker para namorado, Joe transforma-se no homem perfeito para Beck, ao mesmo tempo em que remove sorrateiramente todos os obstáculos no caminho dos dois. Mas também há muito mais em Beck do que sua fachada perfeita, e o relacionamento mutuamente obsessivo do casal rapidamente se desdobra em um turbilhão de consequências mortais. Um relato devastador de uma farsa implacável, Você é um suspense arrebatador sobre vulnerabilidade e manipulação na era das redes sociais, capaz de provar que o amor também pode ferir. E muito."}'

files =  {'file': open('images/voce-you.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

request = '{"book_name": "A sombra do vento", "author": "Carlos Ruiz Zafón", "volume": 1, "version": 1, "category": "Suspense","synopsis": "Barcelona, 1945. Daniel Sempere acorda na noite de seu aniversário de onze anos e percebe que já não se lembra do rosto da falecida mãe. Para consolá-lo, o pai leva o menino pela primeira vez ao Cemitério dos Livros Esquecidos. É lá que Daniel descobre A sombra do vento, romance escrito por Julián Carax, que logo se torna seu autor favorito, sua obsessão. No entanto, quando começa a buscar outras obras do escritor, Daniel descobre que alguém anda destruindo sistematicamente todos os exemplares de todos os livros que Carax já publicou, e que o que tem nas mãos pode muito bem ser o último volume sobrevivente. Junto com seu amigo Fermín, Daniel percorre a cidade, adentrando as ruelas e os segredos mais obscuros de Barcelona. Anos se passam e sua investigação inocente se transforma em uma trama de mistério, magia, loucura e assassinato. E o destino de seu autor favorito de repente parece intimamente conectado ao dele."}'

files =  {'file': open('images/a-sombra-do-vento.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


## Drama

request = '{"book_name": "A Menina que Roubava Livros", "author": "Markus Zusak", "volume": 1, "version": 1, "category": "Drama","synopsis": "A trajetória de Liesel Meminger é contada por uma narradora mórbida, surpreendentemente simpática. Ao perceber que a pequena ladra de livros lhe escapa, a Morte afeiçoa-se à menina e rastreia suas pegadas de 1939 a 1943. Traços de uma sobrevivente: a mãe comunista, perseguida pelo nazismo, envia Liesel e o irmão para o subúrbio pobre de uma cidade alemã, onde um casal se dispõe a adotá-los por dinheiro. O garoto morre no trajeto e é enterrado por um coveiro que deixa cair um livro na neve. É o primeiro de uma série que a menina vai surrupiar ao longo dos anos. O único vínculo com a família é esta obra, que ela ainda não sabe ler."}'

files =  {'file': open('images/a_menina_que_roubava_livros.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "A Culpa É das Estrelas", "author": "John Green", "volume": 1, "version": 1, "category": "Drama","synopsis": "Hazel é uma paciente terminal. Ainda que, por um milagre da medicina, seu tumor tenha encolhido bastante - o que lhe dá a promessa de viver mais alguns anos -, o último capítulo de sua história foi escrito no momento do diagnóstico. Mas em todo bom enredo há uma reviravolta, e a de Hazel se chama Augustus Waters, um garoto bonito que certo dia aparece no Grupo de Apoio a Crianças com Câncer. Juntos, os dois vão preencher o pequeno infinito das páginas em branco de suas vidas."}'

files =  {'file': open('images/a_culpa_e_das_estrelas.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "O diário de Suzana para Nicolas", "author": "James Patterson ", "volume": 1, "version": 1, "category": "Drama","synopsis": "Depois de quase um ano juntos, o poeta Matt Harrison acaba de romper com Katie Wilkinson. A jovem editora, que não tinha qualquer dúvida quanto ao amor que os unia, não consegue entender como um relacionamento tão perfeito pôde acabar tão de repente. Mas tudo está prestes a ser explicado. No dia seguinte ao rompimento, Katie encontra um pacote deixado por Matt na porta de sua casa. Dentro dele, um pequeno volume encadernado traz na capa cinco palavras, escritas com uma caligrafia que ela não reconhece: Diário de Suzana para Nicolas. Ao folhear aquelas páginas, Katie logo descobre que Suzana é uma jovem médica que, depois de sofrer um infarto, decidiu deixar para trás a correria de Boston e se mudar para um chalé na pacata ilha de Martha’s Vineyard. Foi lá que conheceu Matt. E lá nasceu o filho deles, Nicolas. Por que Matt teria lhe deixado aquele diário? Agora, confusa e sofrendo pelo fim do relacionamento, é nas palavras de outra mulher que Katie buscará as respostas para sua vida. O diário de Suzana para Nicolas é uma história de amor que se constrói ao virar de cada página. Cada revelação é mais uma nuance sobre seus personagens. Cada descoberta é um fio a mais a ligar vidas que o destino entrelaçou. **** Sozinha em seu apartamento, Katie abaixou a cabeça quando terminou de ler o diário encadernado em couro. Colocou-o sobre o banquinho de madeira ao lado da banheira. Então começou a soluçar. Sentiu o corpo estremecer. Jamais imaginaria o efeito perturbador que aquelas páginas poderiam ter sobre ela. A imagem de Suzana lhe veio à cabeça. Então pensou no pequeno Nicolas aos 12 meses de idade, com seus olhos azuis brilhantes. Por fim, visualizou Matt. Pai de Nicolas. Marido de Suzana. Ex-namorado de Katie. O que ela pensava de Matt agora? Não tinha certeza. Mas finalmente compreendia um pouco do que havia acontecido. O diário havia apontado pequenos traços do que ela precisava saber e lhe revelara segredos dolorosos de que talvez não quisesse tomar conhecimento. Num romance que vai se reconstruindo a cada revelação, James Patterson conta histórias de amor que surpreendem página a página. Com leveza e sensibilidade, ele entrelaça os destinos da mulher que saiu do interior para fazer carreira em Nova York, da médica que se refugiou em uma ilha em busca de uma vida tranquila e do poeta sensível e carismático que conquistou o coração das duas."}'

files =  {'file': open('images/diario_para_nicolas.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

request = '{"book_name": "Souvenir", "author": "Lily Duncan", "volume": 1, "version": 1, "category": "Drama","synopsis": "Eleonora Baudelaire está no auge dos seus vinte e seis anos, mas acha que já viveu todas as suas aventuras. Sempre pensando em contas para pagar, a jovem musicista ingressa em Psicologia, a sua segunda faculdade. Ela estuda e trabalha integralmente; sem tempo para o amor, sem tempo para os relacionamentos."}'

files =  {'file': open('images/souvenir.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

request = '{"book_name": "Se eu ficar", "author": "Gayle Forman", "volume": 1, "version": 1, "category": "Drama","synopsis": "Depois do acidente, ela ainda consegue ouvir a música. Ela vê o seu corpo sendo tirado dos destroços do carro de seus pais - mas não sente nada. Tudo o que ela pode fazer é assistir ao esforço dos médicos para salvar sua vida, enquanto seus amigos e parentes aguardam na sala de espera... e o seu amor luta para ficar perto dela. Pelas próximas 24 horas, Mia precisa compreender o que aconteceu antes do acidente - e também o que aconteceu depois. Ela sabe que precisa fazer a escolha mais difícil de todas."}'

files =  {'file': open('images/se_eu_ficar.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

request = '{"book_name": "Uma curva no tempo", "author": "Dani Atkins", "volume": 1, "version": 1, "category": "Drama","synopsis": "Às vésperas de saírem da cidade para a faculdade, Rachel Wiltshire e seus amigos sofreram um terrível acidente. Durante o jantar de despedida do grupo, um carro desgovernado atravessou a vidraça do restaurante onde estavam. Rachel escapou por pouco... Na verdade, ela deve sua vida a Jimmy, seu melhor amigo, que se sacrificou para salvá-la."}'

files =  {'file': open('images/uma_curva_tempo.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

request = '{"book_name": "Um caso perdido", "author": "Colleen Hoover", "volume": 1, "version": 1, "category": "Drama","synopsis": "Às vezes, descobrir a verdade pode deixar com menos esperança do que acreditar em mentiras. Sky nunca sentiu verdadeira atração por nenhum dos muitos garotos com quem esteve. Após anos estudando em casa convence sua mãe a fazer o último ano letivo na escola. É quando conhece Dean Holder, um rapaz com uma reputação capaz de rivalizar com a dela. Em um único encontro, ele conseguiu amedrontá-la e cativá-la. E algo nele faz com que memórias de seu passado conturbado comecem a voltar, mesmo depois de todo o trabalho que teve para enterrá-las. Mas o misterioso Holder também tem sua parcela de segredos e quando eles são revelados, a vida de Sky muda drasticamente."}'

files =  {'file': open('images/um_caso_perdido.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

## Terror

request = '{"book_name": "Horror em Amityville", "author": "Jay Anson", "volume": 1, "version": 1, "category": "Terror","synopsis": "Depois de passar algumas décadas fechada, a propriedade no número 112 da Ocean Avenue no subúrbio de Nova York finalmente abre as portas para os leitores da DarkSide Books. Cercada pela natureza, com janelas amplas e uma sacada espaçosa, ela poderia ser uma casa de bairro tranquila como todas as outras, não fosse seu passado devastador e sangrento. Em 1975, George e Kathleen Lutz resolveram recomeçar a vida em uma nova residência que compraram por uma pechincha. Vinte e oito dias depois, os cinco membros da família fugiram aterrorizados, deixando a maior parte de seus pertences para trás. Estranhos eventos começaram a acontecer, afetando a vida dos Lutz e indicando que uma presença maligna habitava a casa. Embora tenha sido amplamente divulgada pela mídia, em especial nos jornais e nas revistas da época, muitas vezes de maneira sensacionalista, a história da casa nunca havia sido contada com riqueza de detalhes — até Jay Anson decidir reconstruí-la e transformar seu livro de não-ficção em um dos relatos paranormais mais importantes e conhecidos de todos os tempos. Baseado nas experiências sobrenaturais reportadas pelos Lutz durante o mês de dezembro de 1975 e o começo de janeiro de 1976, Amityville é um dos livros mais aguardados pelos leitores da Caveirinha. Por isso mesmo, muito mais do que dar apenas aquela demão de tinta, a DarkSide Books vai fazer uma reforma completa na casa, apresentando a sombria construção em detalhes, do quarto secreto no porão às verdadeiras manchas nas portas e nas paredes escondidas pelas tintas do tempo — tudo exatamente como aconteceu, com todos as entidades e vozes que habitaram o sótão, o porão e demais cômodos da casa —, em uma edição assustadora e com o cuidado quase sobrenatural da editora mais dark do Brasil. Adaptada várias vezes para o cinema e contando também com diversos spin-offs, a história de Amityville hoje é amplamente conhecida e é considerada um dos mais importantes relatos sobre casas mal-assombradas da cultura popular."}'

files =  {'file': open('images/horror_amityville_pensador.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "O Desfiladeiro do Medo", "author": "Clive Barker ", "volume": 1, "version": 1, "category": "Terror","synopsis": "O Desfiladeiro do Medo é um livro sem paralelo: uma descrição implacável e irresistível de Hollywood e seus demônios, contada com um estilo cru e o poder narrativo que transformaram os livros e filmes de Clive Barker em fenômenos mundiais. Hollywood transformou Todd Pickett em um astro. O tempo, porém, está lhe cobrando um preço por isso. Ele não tem mais o rosto perfeito do ano anterior. Após uma cirurgia malfeita, Todd precisa de um lugar onde possa esconder-se durante algum tempo, enquanto as cicatrizes desaparecem. Querendo ser momentaneamente esquecido instala-se em uma mansão no Coldheart Canyon, um recanto da cidade tão secreto, que sequer consta nos mapas. Tammy Lauper, presidente de seu fã-clube, chega à cidade de Los Angeles decidida a solucionar o mistério do desaparecimento de Todd. Lá chegando, descobre segredos a respeito do Coldheart Canyon: os espíritos da “Lista A” dos astros e estrelas falecidos de Hollywood que vieram participar de orgias no canyon."}'

files =  {'file': open('images/Desfiladeiro-do-Medo.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "As Ruínas", "author": "Scott Smith", "volume": 1, "version": 1, "category": "Terror","synopsis": "Quatro amigos decidem passar as férias nas praias de Cancun. O programa se torna um verdadeiro pesadelo quando o grupo decide unir-se a Mathias, um alemão que conhecem no hotel, em uma busca por seu irmão, que desapareceu misteriosamente ao tentar encontrar ruínas maias localizadas no coração da selva mexicana. Ao seguir uma trilha na mata, os jovens acabam presos em uma clareira. Com estoques reduzidos de água e comida, e envoltos por um clima de tensão que cresce a cada momento, eles logo percebem que estão sendo observados por alguém. Um ser que conhece seus maiores medos e fraquezas, ávido por sangue e discórdia. Com suas vidas em risco e cercados por um inimigo sem face, dotado de uma inteligência desafiadora, os jovens terão de tenta r impedir que suas tão bem escondidas angústias venham à tona. Um romance sobre as inesperadas reações que as pessoas são capazes de assumir quando confrontadas com uma situação-limite e nossa fragilidade diante do poder da natureza."}'

files =  {'file': open('images/as_ruinas.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))



request = '{"book_name": "O Chamado de Cthulhu", "author": "H.P Lovecraft", "volume": 1, "version": 1, "category": "Terror","synopsis": "O Chamado de Cthulhu A obra máxima de H.P. Lovecraft em uma versão inédita no Brasil, com ilustrações de Salvador Sanz. O conto é uma excelente, e assustadora, “porta de entrada” para o universo lovecraftiano. O escritor é considerado o Pai do Terror Cósmico e sua influência está em toda cultura pop. Diferentemente das outras edições internacionais, a versão brasileira ganhará ilustrações exclusivas do mundialmente conhecido Salvador Sanz. O artista participou de longas e curtas de animação, ilustrou livros, realizou storyboards para cinema/publicidade e publicou diversos quadrinhos, entre eles Legião, Desfigurado, Noturno e Angela Della Morte."}'

files =  {'file': open('images/chamado_cthulhu.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))



request = '{"book_name": "A Profecia", "author": "David Seltzer", "volume": 1, "version": 1, "category": "Terror","synopsis": "E se o anticristo estivesse entre nós? E se ele fosse uma criança e fosse o seu filho? É com enorme orgulho que a editora Pipoca e Nanquim traz de volta A Profecia, obra que é considerada por muitos críticos como uma das três mais importantes da literatura moderna de terror, junto de O Bebê de Rosemary e O Exorcista. Escrito em 1976 por David Seltzer, um mago de Hollywood que trabalhou como roteirista, diretor e produtor, o livro fala sobre o surgimento do Anticristo no mundo de hoje, tomado por guerras, conflitos raciais, turbulências políticas, desigualdades sociais e pragas. Assim que foi publicado, tornou-se um bestseller e meses depois foi adaptado para filme, com direção de Richard Donner (Superman: o Filme, Os Goonies) e protagonizado pelo astro Gregory Peck (Moby Dick, O Sol é para Todos). Após décadas sem ser publicado no Brasil, A Profecia agora retorna numa edição caprichada e luxuosa, com capa dura, verniz localizado e 280 páginas em papel pólen soft."}'

files =  {'file': open('images/a_profecia.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))



request = '{"book_name": "O Bebê de Rosemary", "author": "Ira Levin", "volume": 1, "version": 1, "category": "Terror","synopsis": "Rosemary Woodhouse e seu marido Guy, um ator que luta para se firmar na carreira, mudam-se para um dos endereços mais disputados de Nova York, o Bramford, um edifício antigo de ares vitorianos, habitado em sua maioria por moradores idosos e célebre por uma reputação algo macabra de incidentes misteriosos ao longo da história. Sem demora, os novos vizinhos, Roman e Minnie Castevet, vêm dar boas-vindas aos Woodhouse. Apesar das reservas de Rosemary com relação a seus hábitos excêntricos e aos barulhos estranhos que ouve à noite, o casal idoso logo passa a ser uma presença constante em suas vidas, especialmente na de Guy. Tudo parece ir de vento em popa. Guy consegue um ótimo papel na Broadway, e novas oportunidades não param de surgir para ele. Rosemary engravida, e os Castevets passam a tratá-la com atenção especial. Mas, à medida que a gestação evolui e parece deixá-la mais frágil, Rosemary começa a suspeitar que as coisas não são o que parecem ser... Em 1969, O bebê de Rosemary, fenômeno aclamado por público e crítica, foi adaptado para o cinema em uma produção que se tornou um clássico do terror, estrelada por Mia Farrow e Roman Polanski. Em 2014, a força da história sinistra de Rosemary e seu bebê chegou à TV americana, em uma elogiada minissérie estrelada por Zoe Saldana."}'

files =  {'file': open('images/bebe_rosemery.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))



request = '{"book_name": "O Exorcista", "author": "William Peter Blatty", "volume": 1, "version": 1, "category": "Terror","synopsis": "Um clássico do terror com mais de 13 milhões de exemplares vendidos. Uma obra que mudou a cultura pop para sempre, O exorcista é o livro que deu origem ao maior filme de terror do século XX. Quatro décadas após chocar o mundo inteiro, a obra-prima de William Peter Blatty permanece uma metáfora moderna do combate entre o sagrado e o profano, em um dos romances mais macabros já escritos.. O mal assume várias formas. Seja com monstros, fantasmas ou demônios, tanto a literatura quanto o cinema sempre foram bem-sucedidos em representar a essência do nosso lado mais reprovável. O exorcista, no entanto, conseguiu superar qualquer outra obra do gênero. Inspirado no caso real do exorcismo de um adolescente, o escritor William Peter Blatty publicou em 1971 a perturbadora história de Chris MacNeil, uma atriz que sofre com inesperadas mudanças no comportamento da filha de 11 anos, Regan. Quando todos os esforços da ciência para descobrir o que há de errado com a menina falham e uma personalidade demoníaca parece vir à tona, Chris busca a ajuda da Igreja para tentar livrar a filha do que parece ser um raro caso de possessão. Cabe a Damien Karras, um padre da universidade de Georgetown, salvar a alma de Regan e ao mesmo tempo tentar restabelecer a própria fé, abalada desde a morte da mãe. Neste livro, Blatty conseguiu dar ao demônio a sua face mais revoltante: a corrupção de uma alma inocente. A menina Regan é, ao mesmo tempo, o mal e sua vítima. Ela recebe a pena e a revolta de leitores e espectadores em doses equivalentes e, mesmo quarenta anos depois, seu sofrimento e o abismo entre o que ela era e o que se torna continuam nos atormentando a cada página, a cada cena. Um clássico do terror que se mantém atual como somente os grandes nomes do gênero poderiam criar, O exorcista não se trata apenas de uma simples história sobre o bem contra o mal, ou sobre Deus contra o Demônio, mas também sobre a renovação da fé.."}'

files =  {'file': open('images/exorcista.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

## Auto -  ajuda

request = '{"book_name": "O Poder do Agora", "author": "Eckhart Tolle", "volume": 1, "version": 1, "category": "Auto-ajuda","synopsis": "Nós passamos a maior parte de nossas vidas pensando no passado e fazendo planos para o futuro. Ignoramos ou negamos o presente e adiamos nossas conquistas para algum dia distante, quando conseguiremos tudo o que desejamos e seremos, finalmente, felizes."}'

files =  {'file': open('images/poder_do_agora.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "Quem Mexeu no Meu Queijo?", "author": "Dr. Spencer Johnson", "volume": 1, "version": 1, "category": "Auto-ajuda","synopsis": "Quem mexeu no meu queijo? é um dos maiores sucessos do mercado editorial brasileiro em todos os tempos.Spencer Johnson criou uma história divertida e esclarecedora sobre quatro personagens - dois ratos e dois humanos do mesmo tamanho dos roedores que vivem em um labirinto, numa eterna procura por queijo, que os alimenta e os faz felizes.O queijo é uma metáfora daquilo que se deseja na vida, seja um bom emprego, um relacionamento amoroso, dinheiro, saúde ou paz espiritual. O labirinto é o local onde as pessoas procuram por isso: a empresa onde se trabalha, a família ou a comunidade na qual se vive.Em Quem mexeu no meu queijo?, os personagens se deparam com mudanças inesperadas. Um deles é bem-sucedido e escreve o que aprendeu com sua experiência entre as paredes do labirinto. Suas palavras ensinam a lidar com a mudança para viver com menos estresse e ter mais sucesso no trabalho e na vida pessoal. Escrito para pessoas de todas as idades, Quem mexeu no meu queijo? é uma leitura rápida, mas que traz ensinamentos que vão permanecer por toda a vida."}'

files =  {'file': open('images/quem_mexeu_queijo.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "O Segredo", "author": "Rhonda Byrne", "volume": 1, "version": 1, "category": "Auto-ajuda","synopsis": "Ao longo dos séculos, os fragmentos de um Grande Segredo estiveram presentes nas tradições orais, na literatura, nas religiões e nas correntes filosóficas da humanidade. Agora, pela primeira vez, todas as peças do Segredo foram reunidas em uma revelação extraordinária, capaz de transformar a vida de todos os que a vivenciarem."}'

files =  {'file': open('images/secret.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "Como Fazer Amigos e Influenciar Pessoas", "author": "Dale Carnegie", "volume": 1, "version": 1, "category": "Auto-ajuda","synopsis": "Ao longo de oito décadas, este livro se tornou a referência quando o assunto é o desenvolvimento das relações humanas, das habilidades sociais e da comunicação eficiente."}'

files =  {'file': open('images/como_fazer_amigos.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "O Poder do Hábito", "author": "Charles Duhigg", "volume": 1, "version": 1, "category": "Auto-ajuda","synopsis": "fumar, correu uma maratona e foi promovida. Em um laboratório, neurologistas descobriram que os padrões dentro do cérebro dela mudaram de maneira fundamental. Publicitários da Procter & Gamble observaram vídeos de pessoas fazendo a cama. Tentavam desesperadamente descobrir como vender um novo produto chamado Febreze, que estava prestes a se tornar um dos maiores fracassos na história da empresa. De repente, um deles detecta um padrão quase imperceptível - e, com uma sutil mudança na campanha publicitária, Febreze começa a vender um bilhão de dólares por anos. Um diretor executivo pouco conhecido assume uma das maiores empresas norte-americanas. Seu primeiro passo é atacar um único padrão entre os funcionários - a maneira como lidam com a segurança no ambiente de trabalho -, e logo a empresa começa a ter o melhor desempenho no índice Dow Jones. O que todas essas pessoas tem em comum? Conseguiram ter sucesso focando em padrões que moldam cada aspecto de nossas vidas. Tiveram êxito transformando hábitos. Com perspicácia e habilidade, Charles Duhigg apresenta um novo entendimento da natureza humana e seu potencial para a transformação."}'

files =  {'file': open('images/poder_habito.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "Ansiedade: Como Enfrentar o Mal do Século", "author": "Augusto Cury", "volume": 1, "version": 1, "category": "Auto-ajuda","synopsis": "Vivemos em uma sociedade de excessos. Somos bombardeados por informações que, na maior parte das vezes, não conseguimos absorver. Somos cobrados, pressionados, nos tornamos reféns da nossa mente. Essa situação alterou algo que deveria ser inviolável - o ritmo de construção de pensamentos -, gerando consequências seríssimas para a saúde emocional, o prazer de viver, a inteligência, a criatividade. Pensar é bom, pensar com consciência crítica é melhor ainda, mas pensar excessivamente é uma bomba contra a qualidade de vida e um intelecto criativo e produtivo.Em Ansiedade: como enfrentar o mal do século, o conceituado psiquiatra e psicoterapeuta Augusto Cury apresenta a Síndrome do Pensamento Acelerado (SPA), uma das doenças mais penetrantes da atualidade. Ainda pouco conhecida por psicólogos e psicopedagogos, não raro a SPA é confundida com hiperatividade ou transtorno do déficit de atenção. Neste livro, você conhecerá os sintomas e as consequências desse mal bem, como as técnicas para enfrentá-lo e recuperar sua tranquilidade, emocional e mental."}'

files =  {'file': open('images/ansiedade.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "Por Que Fazemos o Que Fazemos?", "author": "Mário Sergio Cortella", "volume": 1, "version": 1, "category": "Auto-ajuda","synopsis": "Bateu aquela preguiça de ir para o escritório na segunda-feira? A falta de tempo virou uma constante? A rotina está tirando o prazer no dia a dia? Anda em dúvida sobre qual é o real objetivo de sua vida? O filósofo e escritor Mario Sergio Cortella desvenda em Por que fazemos o que fazemos? as principais preocupações com relação ao trabalho. Dividido em vinte capítulos, ele aborda questões como a importância de ter uma vida com propósito, a motivação em tempos difíceis, os valores e a lealdade a si e ao seu emprego. O livro é um verdadeiro manual para todo mundo que tem uma carreira mas vive se questionando sobre o presente e o futuro. Recheado de ensinamentos como Paciência na turbulência, sabedoria na travessia, é uma obra fundamental para quem sonha com realização profissional sem abrir mão da vida pessoal."}'

files =  {'file': open('images/cortella.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

## Romance

request = '{"book_name": "Fazes-me falta", "author": "Inês Pedrosa", "volume": 1, "version": 1, "category": "Romance","synopsis": "O leitor que abre este romance de Inês Pedrosa depara com um dispositivo narrativo de extrema simplicidade: duas vozes apenas, que, ao longo de cinquenta blocos textuais, a que, pela sua episódica brevidade, não chegaremos a chamar capítulos, se cruzam numa espécie de diálogo espectral.Uma dessas vozes é feminina, e é a ela que cabe a iniciativa de convocar os temas. A outra voz, que viremos a saber que é mais velha, pertence a um homem.Poderíamos pensar, segundo as convenções de leitura para que estamos preparados, que entre estas duas personagens existe sobretudo uma relação passional. Mas aquilo que as une é de uma outra ordem - e de certo modo o livro não faz mais do que ir à procura do nome exacto para essa ordem, o nome apropriado para esse tecido de palavras que une, enreda, compromete, envolve estas duas vozes. (...)»«Sem dúvida o seu melhor livro, e desde já um dos romances mais importantes e apaixonantes publicados este ano.» Eduardo Prado CoelhoInês Pedrosa"}'

files =  {'file': open('images/fazes-me-falta.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

request = '{"book_name": "Aritmética", "author": "Fernanda Young", "volume": 1, "version": 1, "category": "Romance","synopsis": "O escritor e professor João Dias encanta-se com a aluna América e se envolve numa história de amor tão cálida quanto platônica, tão real quanto inatingível. Ambos casados, os novos amantes criam uma regra para preservar a clandestinidade: o segundo encontro se daria um mês depois do primeiro, o próximo dali a dois meses e o seguinte após quatro meses, assim sucessivamente."}'

files =  {'file': open('images/aritmetica.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

request = '{"book_name": "Inês da minha alma", "author": "Isabel Allende", "volume": 1, "version": 1, "category": "Romance","synopsis": "Inés da Minha Alma, de Isabel Allende, é um romance épico no qual o alento do amor concede uma trégua à rudeza, à violência e à crueldade de um momento histórico inesquecível. Inés Suárez (1507-1580) é uma jovem e humilde costureira que embarca da Europa ao Novo Mundo em busca de seu marido, desaparecido junto de seus sonhos de glória do outro lado do Atlântico, e acaba se tornando um dos principais nomes da conquista do Chile. Através da pena da mais famosa escritora latino-americana da atualidade, se confirma que a realidade pode ser tão surpreendente quanto a melhor ficção – e igualmente cativante. Em Inés da Minha Alma, Isabel Allende volta a demonstrar seu dom para criar personagens femininos fortes e densos, ao mesmo tempo em que revê a história oficial através de um novo ponto de vista."}'

files =  {'file': open('images/ines-da-minha-alma.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "A rainha Margot", "author": "Alexandre Dumas", "volume": 1, "version": 1, "category": "Romance","synopsis": "Margot é a ponta de três triângulos amorosos de características e dinâmicas próprias (as outras pontas ocupadas por Henrique de Navarra, Henrique de Guisa e Lérac de La Mole). Por meio dessas experiências amorosas, ela passa por um processo de amadurecimento: no início era a jovem princesa Margot, preocupada apenas com seus prazeres; depois do casamento, torna-se a rainha Margarida de Navarra, envolvida diretamente nas intrigas do trono, uma mulher que conhece o amor e a dor."}'

files =  {'file': open('images/a-rainha-margot.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "A assinatura de todas as coisas", "author": "Elizabeth Gilbert", "volume": 1, "version": 1, "category": "Romance","synopsis": "Escritora que atraiu milhões de leitores no mundo inteiro, Elizabeth Gilbert mergulha na ficção, em A assinatura de todas as coisas, para narrar a surpreendente história de uma mulher à frente de seu tempo, determinada a desvendar não só os mais íntimos segredos da natureza, mas também do amor. Alma Whittaker nasceu na virada dos anos 1800, nos Estados Unidos, filha de um ambicioso botânico que construiu por conta própria uma das maiores fortunas da Filadélfia. Curiosa desde criança, e instruída com rigor pela mãe holandesa, ela aos poucos abraça a mesma devoção do pai e, sozinha, se dedica ao estudo das ciências naturais. Mas algo falta em sua vida. Desiludida no amor, reservada e solitária, Alma conhece um jovem sonhador, exímio desenhista de orquídeas que, assim como ela, é fascinado pelo mundo ao seu redor. Esse é o início de uma intricada e trágica relação, que a levará até os confins da Terra para descobrir não apenas algo sobre ele, mas sobre sua própria natureza. A partir de uma pesquisa minuciosa, e com uma escrita fluente e cativante, Elizabeth Gilbert desfila personagens inesquecíveis: missionários, abolicionistas e aventureiros; gênios e loucos, sonhadores e excêntricos. Ao transportar o leitor para outra época e outras culturas, ela o faz descobrir, assim como Alma, os segredos que a aguardam nos confins desse mundo inexplorado."}'

files =  {'file': open('images/a-assinatura-de-todas-as-coisas-elizabeth-gilbert.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))


request = '{"book_name": "A abadia de Northanger", "author": "Jane Austen", "volume": 1, "version": 1, "category": "Romance","synopsis": "Escrito ainda na juventude de Jane Austen e publicado postumamente, em 1818, A Abadia de Northanger é, sem dúvida, um dos romances mais elaborados da época – uma comédia satírica que aborda questões humanas de maneira sutil, tendo como pano de fundo a cidade de Bath. O enredo gira em torno de Catherine Morland, que deixa a tranquila e, por vezes, tediosa vida na zona rural da Inglaterra para passar uma temporada na agitada e sofisticada Bath do final do século XVIII. Catherine é uma jovem ingênua, cheia de energia e leitora voraz de romances góticos. O livro faz uma espécie de paródia a esses romances, especialmente os escritos por Ann Radcliffe. Jane Austen faz um eloquente contraste entre realidade e imaginação, entre uma vida pacata e as situações sinistras e excitantes que os personagens de um romance podem viver."}'

files =  {'file': open('images/a-abadia-de-northanger.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

request = '{"book_name": "Dona Flor e seus dois maridos", "author": "Jorge Amado", "volume": 1, "version": 1, "category": "Romance","synopsis": "Um dos romances mais populares de Jorge Amado, levado com êxito ao cinema, ao teatro e à televisão, Dona Flor e seus dois maridos conta a história de Florípedes Paiva, que conhece em seus dois casamentos a dupla face do amor: com o boêmio Vadinho, Flor vive a paixão avassaladora, o erotismo febril, o ciúme que corrói. Com o farmacêutico Teodoro, com quem se casa depois da morte do primeiro marido, encontra a paz doméstica, a segurança material, o amor metódico. Um dia, porém, Vadinho retorna sob a forma de um fantasma capaz de proporcionar de novo à protagonista o êxtase dos embates eróticos. Por obra da fantasia literária de Jorge Amado e da intervenção das entidades do candomblé, Flor consegue conciliar no amor o fogo e a calmaria, a aventura e a segurança, a paixão e a gentileza. Lançada em 1966, esta narrativa ousada e exuberante, plena de humor e ironia, é uma saborosa crônica de costumes da Bahia da primeira metade do século XX e um retrato inventivo das ambigüidades que marcam o Brasil."}'

files =  {'file': open('images/dona-flor-e-seus-dois-maridos.jpg', 'rb')}
response = requests.post('http://localhost:3000/add_books', data= {"request":request},files=files)
print("status: {}".format(response.status_code))

