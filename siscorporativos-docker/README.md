## Informações sobre os containers e imagens das aplicações

### Executar aplicações, e baixar dependências
  - Clonar o repositório ```https://github.com/sistemascorporativos3a/docker``` em sua máquina local
  - Para executar todos os módulos, utilize o comando:
    ```
    docker-compose up
    ```
  - Para executar individualmente um dos módulos, utilize o comando:
    ```
    docker-compose -f docker-compose-modulo-{nome}.yml up
    ```

  - Observações:
    - Para baixar as imagens dos containers é necessário possuir uma conta no serviço _Docker Hub_ https://hub.docker.com/;
    - Antes de baixar as imagens, realize o login em sua estação com o comando ```docker login```;
    - Adicione o parâmetro "-d" ao comando ```docker-compose up``` para executar em modo background os serviços;
    - Lista de comandos úteis no Docker:
      ```
      docker login
      docker ps
      docker images
      docker rmi -f {id}
      docker exec -it {imagem} bash
      docker stop {container}
      docker-compose up
      docker-compose down
      ```

### Repositório dos containers (DockerHub)

https://hub.docker.com/u/sistemasdeinformacao/

- Imagens:
  ```
  sistemasdeinformacao/mysql-adventure-works
  sistemasdeinformacao/modulo-admin
  sistemasdeinformacao/modulo-compras
  sistemasdeinformacao/modulo-inventario
  sistemasdeinformacao/modulo-pessoas
  sistemasdeinformacao/modulo-produtos
  sistemasdeinformacao/modulo-producao
  sistemasdeinformacao/modulo-rh
  sistemasdeinformacao/modulo-vendas
  ```
- Dependências:
  ```
  mysql:5.6
  rabbitmq:3-management
  springcloud/eureka
  ```
- Download individual do container:
  ```
  docker pull sistemasdeinformacao/{nome da imagem}
  ```

### Acesso ao container MySQL para executar comandos SQL, caso necessário
  - Host:
    ```localhost```
  - Porta:
    ```3307```
  - Acesso via linha de comando quando a imagem for iniciada pelo docker-compose:
    ```
    mysql --host=localhost --protocol=TCP --port=3307 -u root -p
    ```
  - Acesso via linha de comando quando a imagem for iniciada manualmente:
    ```
    mysql --host=localhost --protocol=TCP --port=3306 -u root -p
    ```
  - Observações:
    - Usuário: root
    - Senha:   root
    
    
### Endereço das aplicações
  - Verificar URLs das aplicações no serviço Eureka: http://localhost:8761/
  
  - *Observações: As rotas das aplicações estão nos arquivos README.md dos repositórios*
