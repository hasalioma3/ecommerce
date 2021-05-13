class Person {
    constructor(
        protected firstName:string, 
        protected lastName:string, 
        protected age: number
        ){}

    getFullName(): string {
        return `${this.firstName} ${this.lastName}`;

    }

}

const person: Person = new Person(`John`, `Doe`, 25);
console.log(person.getFullName());
console.log(person);

//inheritence
class Employee extends Person{
    constructor(
        private id:number,
        firstName: string,
        private middleName:string,
        lastName: string,
        age:number
    ){
        super(firstName, lastName, age);
    }
    getFullName(): string{
       
        return `${this.firstName} ${this.middleName} ${this.lastName}`;
    }
}

const manager:Person= new Employee(1, `jane`,`Patrick`,`Doe`, 30);
console.log (`${manager.getFullName()}`);