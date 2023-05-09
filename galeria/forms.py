from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from galeria.models import Sono, Exercise, Planejamento

class SonoForm(forms.ModelForm):
    class Meta:
        model = Sono
        fields = ['dormiu', 'acordou']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}),max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    def create_exercises(self, user):
        #olhar DEPOIS questao de sets, reps, etc
        Exercise.objects.create(user=user, name='supino reto barra', group='peitoral', sets=3, reps=10, rest='40s', weight=10,description = 'uma flexão de ombro horizontal seguida por uma extensão de cotovelo enquanto segura a barra na linha do pescoço, realizar esse movimento empurrando a barra para cima, em seguida, de forma lenta e controlada, retornar a posição inicial', link = 'https://www.youtube.com/embed/sqOw2Y6uDWQ')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='supino inclinado halter + crucifixo halter', group='peitoral', sets=3, reps=12, rest='40s', weight=15, description = 'segurando o par de halteres, abrir os braços até mais ou menos o cotovelo chegar na mesma linha dos ombros, sem esquecer de manter os braços ligeiramente flexionados.', link = 'https://www.youtube.com/embed/Z1rCZ0YHrP0' )
        Exercise.objects.create(user=user, name='tríceps máquina', group='peitoral', sets=3, reps=12, rest='40s', weight=15, description = 'Deixe os cotovelos apontados para trás e apoie as costas no encosto do banco. Por fim, segure nas alças com as palmas das mãos voltadas para o centro do corpo, em seguida empurre as alças para baixo enquanto contrai os tríceps e solta o ar. Quando seus braços estiverem quase totalmente esticados, faça uma breve pausa e retorne lentamente à posição inicial, inspirando o ar', link = 'https://www.youtube.com/embed/oBF4YIwh_w8')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='elevação frontal', group='peitoral', sets=3, reps=12, rest='40s', weight=15,description = ' com os halteres na mão com pegada pronada e braços estendidos, o movimento de flexão de ombros, elevando os braços até estes estarem paralelos ao solo, mais ou menos no ângulo de 90 graus, e Descer de maneira controlada os braços até estes estarem novamente na posição inicial', link = 'https://www.youtube.com/embed/0K9NJHXYSm4')#title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='tríceps francês', group='peitoral', sets=3, reps=12, rest='40s', weight=15, description = 'Levante a barra EZ ou o halter diretamente acima de sua cabeça. Dobre os cotovelos e abaixe a barra atrás da cabeça antes de levantá-la novamente. Mantenha a parte do braço entre ombro e cotovelo parada', link = 'https://www.youtube.com/embed/D2oQJTz-RCA')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='desenvolvimento arnold', group='peitoral', sets=3, reps=12, rest='40s', weight=15,description = 'De pé ou sentado, segurar um halter em cada mão com a pegada supinada, estes devem estar à frente do corpo, na altura dos ombros.A coluna deve estar em posição neutra e assim deve permanecer durante todo o exercício. Iniciar o exercício empurrando para cima os halteres e girando os punhos durante o movimento, Ao chegar ao fim da fase concêntrica as mãos devem estar em pegada pronada acima da cabeça e os cotovelos devem estar quase que completamente, estendidos, Retornar lentamente a posição inicial', link = 'https://www.youtube.com/embed/YghvTx_GI2c')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='puxada fechada', group='costas', sets=3, reps=12, rest='40s', weight=15,description = 'Segurar a barra com a pegada supinada, depois Trazer a barra mais ou menos até a região superior do peitoral, contraindo ao máximo a dorsal, Estender os braços lentamente até que estejam acima da cabeça novamente.', link = 'https://www.youtube.com/embed/v1rPzvJvwIE')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='remada com apoio aberta + fechada', group='costas', sets=3, reps=12, rest='40s', weight=15,description = 'inicie aduzindo as escápulas (aproximando-as), Comece o movimento de remada, junto com o de flexão dos cotovelos, Neste caso, o movimento é uma abdução de ombros, o movimento é uma extensão de ombros', link = 'https://www.youtube.com/embed/_g6GeyWVivI')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='pullover polia + remada curvada', group='costas', sets=3, reps=12, rest='40s', weight=15,description = 'Inclina seu tronco a frente, Segurando a barra, você vai manter sua coluna estável e com as curvaturas lombares preservadas. Puxe a barra de encontro a abdômen, flexionando os cotovelos e “fechando” (abduzindo) as escápulas.', link = 'https://www.youtube.com/embed/y-XZnuKx3Q0') #title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='rosca direta halter + braquial halter', group='costas', sets=3, reps=12, rest='40s', weight=15,description = 'Segurando um halter em cada mão, estenda totalmente os braços para baixo. Em seguida, flexione os cotovelos levantando os dois halteres simultaneamente até atingir a altura dos ombros e mantenha a posição por alguns segundos. ', link = 'https://www.youtube.com/embed/ilyxkSNoyL8?start=43')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='rosca scoth máquina', group='costas', sets=3, reps=12, rest='40s', weight=15,description = 'Apoiar ambos os braços no recosto de maneira que eles fiquem apoiados até a altura do cotovelo.Segurar a barra (da maquina) com as duas mãos em pegada supinada (palma da mão virada para cima), Flexionar os cotovelos, trazendo o peso para cima até contrair o bíceps ao máximo, Estender os cotovelos de maneira controlada até retornar à posição inicial.', link = 'https://www.youtube.com/embed/3GfAZv126D0?start=43')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='hack', group='perna', sets=3, reps=12, rest='40s', weight=15,description = 'Comece com as costas apoiadas nas almofadas do aparelho. Deixe os pés afastados a uma distância maior que a largura do quadril, Assim, segure nas alças laterais com as mãos para obter apoio e segurança, inspire, levante e destrave o aparelho, Em seguida, inicie o movimento de agachamento lentamente até atingir um ângulo menor que 90 graus com os joelhos, Depois, retorne à posição inicial.', link = 'https://www.youtube.com/embed/QZglgfUQZdk?start=43')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>' )
        Exercise.objects.create(user=user, name='leg 45°', group='perna', sets=3, reps=12, rest='40s', weight=15,description = 'Sentar no aparelho, com as costas apoiadas e os pés posicionados na plataforma na mesma linha dos quadris, Destravar o aparelho e iniciar o movimento para flexionar o joelho até estes se encontrarem mais ou menos em um ângulo de 90 graus, Estender o joelho e depois flexioná-los novamente.', link = 'https://www.youtube.com/embed/kyESFAj3W0E?start=43')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='extensora', group='perna', sets=3, reps=12, rest='40s', weight=15,description = 'Em primeiro lugar é necessário regular o banco de acordo com a altura de cada indivíduo, de forma que a parte de trás do joelho esteja exatamente na região da dobra da cadeira, Sentado na cadeira, as costas devem estar bem apoiadas e respeitando a curvatura fisiológica da coluna, Iniciando o exercício, estenda os joelhos até a contração máxima do músculo, Retorne de maneira controlada á posição inicial.', link = 'https://www.youtube.com/embed/1f1DjMr68hY?start=43')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='flexora', group='perna', sets=3, reps=12, rest='40s', weight=15,description = 'Sentar no aparelho, apoiando bem a coluna, os pés devem estar apoiados em cima da almofada, com esta na altura da linha dos tornozelos.Prestar atenção também ao travar a almofada que apóia na coxa, pois esta deve estar logo acima do joelh, Flexionar os joelhos até contrair ao máximo o músculo da posterior da coxa, Retornar lentamente a posição inicial estendendo os joelhos de maneira controlada.', link = 'https://www.youtube.com/embed/n8j1X_xByD4?start=43')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='cadeira abdutora', group='perna', sets=3, reps=12, rest='40s', weight=15,description = 'Sente-se na máquina, posicione os pés nos apoios, suba a trava e una as pernas vagarosamente. Para o movimento de abdução, você deve fazer força empurrando a máquina para fora, afastando os joelhos. Depois você deve voltar à posição inicial lentamente, mantendo a tensão dos músculos em vez de soltar o peso da máquina de uma vez.', link = 'https://www.youtube.com/embed/yVZ0Vs7j6EM?start=43')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')
        Exercise.objects.create(user=user, name='elevação panturrilha', group='perna', sets=3, reps=12, rest='40s', weight=15,description = 'De pé, coloque uma mão na cintura e outra nas costas da cadeira servindo como apoio. Coloque o peso do corpo sobre a planta de um dos pés e eleve o calcanhar o mais alto que conseguir até a outra perna sair do chão, depois retorne a posição inicial lentamente', link = 'https://www.youtube.com/embed/h7bZ4XbuZLg?start=43')# title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            self.create_exercises(user)
        return user

class PlanejamentoForm(forms.ModelForm):
    class Meta:
        model = Planejamento
        fields = ('data', 'horario')
