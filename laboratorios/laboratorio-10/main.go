package main

import (
	"fmt"

	"github.com/brianvoe/gofakeit"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

// MyCats definition for 'my_cats' table
type MyCats struct {
	ID     uint `gorm:"primaryKey"`
	Nombre string
	Imagen string
}

func (mc MyCats) String() string {
	return fmt.Sprintf("ID: %d\nNombre: %s\nImágen: %s\n", mc.ID, mc.Nombre, mc.Imagen)
}

func main() {
	gofakeit.Seed(0)
	dsn := "host=localhost user=the_cat password=secretcat123 dbname=random_cats port=5432 sslmode=disable"
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		panic(err)
	}

	// Creamos un registro
	random := MyCats{
		Nombre: gofakeit.Name(),
		Imagen: gofakeit.ImageURL(1080, 1080),
	}

	// Lo insertamos en la DB
	db.Create(&random)
	// Imprimimos registro
	fmt.Print(random)

	// Insertamos múltiples registros y los imprimimo
	mycats := []MyCats{
		{
			Nombre: gofakeit.Name(),
			Imagen: gofakeit.ImageURL(gofakeit.Number(1000, 3000), gofakeit.Number(1000, 3000)),
		},
		{
			Nombre: gofakeit.Name(),
			Imagen: gofakeit.ImageURL(gofakeit.Number(1000, 3000), gofakeit.Number(1000, 3000)),
		},
		{
			Nombre: gofakeit.Name(),
			Imagen: gofakeit.ImageURL(gofakeit.Number(1000, 3000), gofakeit.Number(1000, 3000)),
		},
	}
	db.Create(&mycats)
	for _, mycat := range mycats {
		fmt.Println(mycat)
	}

	// Buscamos un registro en específico
	var toFind MyCats
	db.Find(&toFind, 2)
	fmt.Println(toFind)

	// Actualiza un registro
	toFind.Imagen = gofakeit.URL()
	db.Save(&toFind)
	fmt.Println(toFind)

	// Borra un registro
	db.Where("Imagen = 'https://picsum.photos/1080/1080'").Delete(&MyCats{})
}
