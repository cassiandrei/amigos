# Similars - Aproximando interesses, criando amizades

Similars, uma rede social que tem por objetivo aproximar as pessoas por seus interesses, gostos e forma de viver. Uma forma de resignificar as relações criadas virtualmente, estimulando interações reais entre as pessoas, conectando-as não somente virtualmente mas também na realidade.

<p align="center">
  <img alt="VS Code in action" src="prints/login.png">
</p>

## Estrutura do projeto
O projeto do **Similars** foi desenvolvido obedecendo a seguinte divisão:
### Autenticação
### Captura das informações dos usuários
### Interface

## Recursos utilizados

O projeto destina-se a ser uma aplicação web responsivo, desenvolvido por meio da utilização do framework web [Django](https://www.djangoproject.com/), em sua versão 1.11.5.

Dado o tempo restrito para o desenvolvimento da ideia, optou-se pela utilização do Facebook como fonte de dados, já que o mesmo possui várias informações relacionadas a cada um dos perfis que possui cadastrado e, para a captura dessas informações de cada perfil, foram utilizadas as API's que são fornecidas pela rede social, tanto para a autenticação facilitada quanto para a utilização dos dados dos perfis dos seus usuários. As API's do Facebook utilizadas são:

* [Facebook Graph API]
(https://developers.facebook.com/docs/graph-api/?locale=pt_BR)
* [Facebook Login]
(https://developers.facebook.com/docs/facebook-login/)

Para o projeto do layout, utilizou-se como base alguns componentes do template Bootstrap [**Gentelella Alela!**](https://colorlib.com/polygon/gentelella/)


## Monetização

Como features do projeto pretende-se adicionar formas de monetização ao software. Para a geração de receita por meio da aplicação optou-se pela mesclagem das principais formas atualmente utilizadas para aplicativos que não exigem pagamento por sua utilização, são elas:

* Anúncios, distribuidos em pontos estratégicos e discretos na página, sem o comprometimento da experiência do usuário

* Monitoramento e análise dos dados gerados pela interação usuário-aplicação, uma alternativa seria o (**Google Analytics**)[https://www.google.com.br/intl/pt-BR_ALL/analytics/learn/index.html]  

