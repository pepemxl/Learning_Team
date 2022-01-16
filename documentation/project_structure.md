# Como manejaremos la estructura de nuestros proyectos.

Tendremos un docker-compose.yml en la raiz de todos los subproyectos, y cada subproyecto contendrá a su vez el Dockerfile necesario para crear el servicio
```
myproject/
  - auth/
    - Dockerfile
  - marketing/
    - Dockerfile
  - billing/
    - Dockerfile
  - contact/
    - Dockerfile
  - user/
    - Dockerfile
  - docker-compose.yml
```

De esta manera cada servicio contiene su propio `Dockerfile`, pero todos ellos estan en el mismo proyecto. Y cada proyecto estar escrito en su propio lenguaje!!!


Por ejemplo para un proyecto de Go donde utilizamos distintos proveedores una estructura podria ser la siguiente:

```
.
├── Dockerfile
├── Makefile                                              <-- Makefile for GO
├── README.md
├── app                                                   <-- Service/Provider package/API
│·· ├── grpc                                              <-- GRPC Server Package
│·· │·· └── server.go
│·· ├── impls                                             <-- Implementations
│·· │·· ├── cache
│·· │·· │·· ├── cacheRedisService.go
│·· │·· │·· └── cacheRedisService_test.go           
│·· │·· └── parameter
│·· │··     ├── environmentParameterService.go
│·· │··     └── environmentParameterService_test.go
│·· ├── mocks                                             <-- Mocks for testing
│·· │·· ├── mock_cacheServicesMock.go
│·· │·· ├── mock_httpClientMock.go
│·· │·· └── mock_parameterServicesMock.go
│·· ├── models                                            <-- Structures for provider request and response 
│·· │·· └── providerModels.go                             
│·· ├── provider                                          <-- Businnes Logic
│·· │·· ├── provider.go   
│·· │·· └── provider_test.go                              
│·· ├── services                                          <-- Service Interfaces                              
│·· │·· ├── cacheService.go
│·· │·· ├── integrationService.go
│·· │·· └── parameterService.go
│·· └── utils                                             <-- Utils libraries
│··     ├── utils.go
│··     └── utils_test.go
├── buildspec-dev.yml                                     <-- yaml file with build/deploy specifications for development
├── buildspec-local.yml                                   <-- yaml file with build/deploy specifications for local
├── buildspec-staging.yml                                 <-- yaml file with build/deploy specifications for stagging
├── buildspec-prod.yml                                    <-- yaml file with build/deploy specifications for production
├── config                                                <-- Source config files for each kind of environment
│·· ├── dev.json
│·· ├── local.json
│·· ├── staging.json
│·· └── prod.json
├── go.mod
├── go.sum
├── grpc-client                                           <-- GRPC client "local test"
│·· └── main.go
└── main.go                                               <-- Main go file
```


