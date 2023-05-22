# THEORY
- Przetwarzanie analogowo-cyfrowe A/C (analog to digital) służy do zamiany sygnału analogowego na sygnał cyfrowy. 
Dzięki temu możliwe jest przetwarzanie ich w urządzeniach elektronicznych opartych o architekturę zero-jedynkową oraz gromadzenie ich na cyfrowych nośnikach danych.

- Proces ten polega na uproszczeniu sygnału analogowego do postaci skwantowanej (dyskretnej), czyli 
zastąpieniu wartości zmieniających się płynnie do wartości zmieniających się skokowo w odpowiedniej 
skali (dokładności) odwzorowania.

- Przetwarzanie A/C tworzą 3 etapy:
	- próbkowanie
	- kwantyzacja
	- kodowanie
	
- Działanie przeciwne do wyżej wymienionego wykonuje przetwornik cyfrowo-analogowy C/A.
Urządzenia służace do tego celu nazywa się przetwornikami.

- Rozdzielczość przetwornika określa się poprzez liczbę dyskretnych wartości jakie może on wytworzyć. 
 Zwykle wyraża się ją w bitach.
 
Przykładowo, przetwornik A/C, który potrafi przetworzyć próbkę sygnału na jedną z 256 wartości liczbowych posiada rozdzielczość równą 8 bitów.

- W komputerach osobistych wyposażonych w karty graficzne możliwa jest kwantyzacja 8 i 16 bitowa.

- Analogowy sygnał jest ciągły w czasie, więc konieczne jest przetworzenie go na ciąg liczb. 
- To, jak często sygnał jest sprawdzany i zamieniany na liczbę zależną od jego poziomu, określane jest mianem częstotliwości próbkowania.

- Innymi słowy można powiedzieć, że częstotliwość próbkowania jest odwrotnością różnicy czasu pomiędzy dwiema kolejnymi próbkami.

- Zwykle nie jest możliwe odtworzenie dokładnie takiego samego sygnału na podstawie wartości liczbowych, ponieważ dokładność jest ograniczona przez błąd kwantyzacji.

- Jednak wiarygodne odwzorowanie sygnału jest możliwe do osiągnięcia, gdy częstotliwość próbkowania jest większa niż podwojona, najwyższa składowa częstotliwość sygnału (twierdzenie Nyquista-Shannona).

# EXERCISE

- Należy zbudować moduł przetwornika A/C i C/A realizujący konwersję dźwięku z postaci analogowej do postaci cyfrowej i odwrotnie.

- Realizowany za pomocą karty dźwiękowej.

- Dźwięk płynący do karty dźwiękowej z mikrofonu lub innego urządzenia zostaje poddany przetwarzaniu A/C i przesyłany w postaci strumienia do dalszego przetwarzania. 

- Możliwe jest uproszczenie tego procesu i zapisanie go w postaci pliku waw zawierającego spróbkowany i skwantowany dzwięk.

- Należy użyć możliwie jak największej ilości możliwych poziomów kwantyzacji i częstotliwości próbkowania i umieścić wyniki w sprawozdaniu.

- Dodatkowo można obliczyć wartość współczynnika SNR dla każdego otrzymanego wyniku względem sygnału o najlepszych parametrach.

# REQUIRED THEORY
- Zasady przetwarzania analogowo-cyfrowego. 
- Znajomość terminów kwantyzacja, próbkowanie, kodowanie, twierdzenie Nyquista-Shannona. 
- Umiejętność oszacowania błędów wynikających z użycia procesów kwantyzacji i próbkowania.
- Znajomość obliczenia współczynnika stosunku sygnał szum (SNR signal to noise ratio) i obliczania błędu średniokwadratowego.