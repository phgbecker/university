# Trabalho de Docker - Sistemas Convergentes

- Integrantes:
  - Pedro Henrique Goes Becker
  - Thainá Batista Carneiro


**Executar containers:**

```#docker-compose up -d```


**Criar banco de dados e popular as tabelas:**

```#docker exec -i docker_mysql-docker_1 mysql -uroot -proot < ./bancoDados/clinica_struct.sql```

```#docker exec -i docker_mysql-docker_1 mysql -uroot -proot < ./bancoDados/clinica_insert.sql```


**Endereço da aplicação:**

http://localhost:8080/ClinicaFrontend


**Remover containers:**

```#docker-compose down```


**Observação:**

_Habilitar CORS no navegador para evitar erros de "Cross-Origin Request Blocked"_
