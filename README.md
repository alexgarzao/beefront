# beefront

BeeFront é um complemento do [Behave](http://pythonhosted.org/behave/). A ideia deste repo é centralizar steps comuns a vários apps.

A visão de futuro é ter um pacote instalável via pip. Mas, por enquanto, o que temos é um processo um pouco chato, mas que é  feito uma vez apenas :-)

```
mkdir -p bdd/
echo bdd/beefront >> .gitignore
echo behave.ini >> .gitignore
cd bdd
git clone https://github.com/alexgarzao/beefront.git
cp -Rf beefront/root_project/ .
touch sequence.featureset

echo "Nao esqueca de instalar o behave no seu virtualenv (pip install behave)"
```

## TODO
* O script acima pode receber o nome do diretório
* Poder baixar o script de algum lugar
* E se fossem 2 coisas separadas: um é o template para usar o projeto, e outro fosse uma lib só com os steps? A lib poderia ser instalada separadamente...
* Aliás, sendo uma lib, nada impede que tenhamos vários libs genéricas (web, API, Android, iOS, ...), ou mesmo com steps focados em regras de negócio
* No template de uso, seria mostrado como importar os steps genéricos no environment.py


## Links úteis para pesquisa
* Exemplo de step library: https://github.com/longaccess/longaccess-behave
* https://stackoverflow.com/questions/36613050/modular-structure-for-behave-tests
* https://github.com/behave/behave/issues/306
* https://github.com/behave/behave/issues/169
* https://github.com/behave/behave/issues/395
* https://github.com/behave/behave/blob/master/features/step.use_step_library.feature
* https://github.com/camptocamp/oerpscenario/commit/aa6e80b90cf7124bfbb984b38c3b74460946a270
* https://github.com/behave/behave/issues/248
* https://github.com/behave/behave/pull/600/commits/02bc64e3f4cc1938854b7bf532025dac297ab6e3
* https://github.com/behave/behave/pull/170/files
* https://github.com/behave/behave/pull/600
* https://github.com/behave/behave/blob/master/features/step.use_step_library.feature
