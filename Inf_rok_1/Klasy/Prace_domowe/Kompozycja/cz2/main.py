from auto import Auto


auto = Auto("Ala")
auto.all_information()

auto.__wlascicel = "Tomek !!!!!!!!!!!!!"

auto.all_information()

print("<"*40)
auto.__silnik.informacje()
print("<"*40)

auto.zmien_informacje()

auto.all_information()

# -----------------------------------------------------------------
from matemtyka import Matemtyka

print(Matemtyka.delta(5,5,5))