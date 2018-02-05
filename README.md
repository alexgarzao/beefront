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

