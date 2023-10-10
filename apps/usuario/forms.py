from typing import Any
from django import forms


class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: Robinson de Sena"}
        ),
    )

    senha = forms.CharField(
        label="Senha de usuário",
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Digite sua senha"}
        ),
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome de Login",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Ex.: Robinson de Sena"}
        ),
    )
    email = forms.CharField(
        label="Digite seu email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "robinsondesena@xpto.com"}
        ),
    )
    senha_1 = forms.CharField(
        label="Crie sua senha",
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Crie uma senha"}
        ),
    )
    senha_2 = forms.CharField(
        label="Cofirmar senha",
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirme sua senha"}
        ),
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get("nome_cadastro")

        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError(
                    "Não é possível inserir espaços nesse campo"
                )
            else:
                return nome
            
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')
        
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("Senhas Diferentes")
            else:
                return senha_2
            
                 
