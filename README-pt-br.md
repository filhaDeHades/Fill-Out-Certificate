# Script para o Preenchimento de Certificados

Read this in [English](https://github.com/filhaDeHades/Fill-Out-Certificate/blob/main/README.md).

Esse repositório foi criado a partir da necessidade de automatizar o preenchimento de certificados emitidos por eventos organizados.
Ação que caso feita manualmente é demorada e massante.

## Como utilizar:

No repositório estão todos os arquivos necessários para que você consiga testar o script.

- **Modelo do Certificado:**
O modelo encontrado no repositório (modelo-certificado.jpg) serve como base para a criação de um modelo próprio (utilizando a mesma altura para o nome do participante). Assim não é necessário fazer nenhuma alteração no código quanto a altura na qual o nome será escrito.

Caso seja utilizado um modelo cuja altura para o nome (onde a linha se encontra) esteja em uma posição diferente, basta mudar a constante ``NAME_HEIGHT`` no código (é recomendado diminuir 2 pixels da altura real para melhor conforto estético).

É recomendado que seja utilizado um arquivo ".jpg" ou ".jpeg" como modelo. Caso um arquivo ".png" seja usado é necessário fazer a conversão de RGBA para RGB.

- **Arquivo de Input**:
O arquivo de inputs contém na **primeira linha** o nome do **arquivo modelo** e nas **linhas seguintes** contém os **nomes** a serem adicionados nos arquivos (um nome em cada linha).