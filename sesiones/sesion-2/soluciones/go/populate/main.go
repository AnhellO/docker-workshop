package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson/primitive"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"go.mongodb.org/mongo-driver/mongo/readpref"
)

// Pet represents a pet
type Pet struct {
	ID     primitive.ObjectID `bson:"_id"`
	Name   string             `json:"name,omitempty" bson:"name,omitempty"`
	Owner  string             `json:"owner,omitempty" bson:"owner,omitempty"`
	Specie string             `json:"specie,omitempty" bson:"specie,omitempty"`
}

var collection *mongo.Collection

func init() {
	client, err := mongo.NewClient(options.Client().ApplyURI("mongodb://m1:27017/"))
	if err != nil {
		panic(err)
	}

	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()

	err = client.Connect(ctx)
	if err != nil {
		panic(err)
	}

	if err := client.Ping(ctx, readpref.Primary()); err != nil {
		panic(err)
	}

	fmt.Println("Successfully connected and pinged.")
	collection = client.Database("mi-db").Collection("pet")
}

func main() {
	insertManyResult, err := collection.InsertMany(
		context.TODO(),
		[]interface{}{
			Pet{
				ID:     primitive.NewObjectID(),
				Name:   "firulais",
				Owner:  "jahir",
				Specie: "perro",
			},
			Pet{
				ID:     primitive.NewObjectID(),
				Name:   "taco",
				Owner:  "jonathan",
				Specie: "perro",
			},
			Pet{
				ID:     primitive.NewObjectID(),
				Name:   "garfield",
				Owner:  "erick",
				Specie: "gato",
			},
			Pet{
				ID:     primitive.NewObjectID(),
				Name:   "charlotte",
				Owner:  "juan daniel",
				Specie: "araña",
			},
			Pet{
				ID:     primitive.NewObjectID(),
				Name:   "solovino",
				Owner:  "jorge",
				Specie: "cuyo",
			},
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Inserted multiple documents: ", insertManyResult.InsertedIDs)
}
