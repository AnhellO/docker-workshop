package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"go.mongodb.org/mongo-driver/bson"
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
	// Obtén un registro
	var result Pet

	err := collection.FindOne(context.TODO(), bson.D{{}}).Decode(&result)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("Imprime un registro: %+v\n", result)

	// Obtén todos los registros
	cur, err := collection.Find(context.TODO(), bson.D{{}}, options.Find())
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Imprime todos los registros")
	for cur.Next(context.TODO()) {
		var elem Pet
		err := cur.Decode(&elem)
		if err != nil {
			log.Fatal(err)
		}

		fmt.Printf("%+v\n", elem)
	}

	if err := cur.Err(); err != nil {
		log.Fatal(err)
	}

	cur.Close(context.TODO())
}
