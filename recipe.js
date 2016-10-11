function recipe(name,ingredients,instructions,serving_size,properties,print_recipe)
{
	this.name=name;
	this.ingredients=ingredients;
	this.instructions=instructions;
	this.serving_size=serving_size;
	this.properties=properties;
	this.print_recipe = 	function() {
		return this.name+"\nServes "+this.serving_size+" people.\nIngredients: "+this.ingredients+"\n"+this.instructions+"\n";
	}
}

/*var ApandBan=new recipe("Apples and Bananas",["Apples","Bananas"],"Eat",3,["Snack","Dinner"]);
var nothing=new recipe("Nothing",[],"Do nothing",0,"Nothing");
console.log(ApandBan.print_recipe());
console.log(nothing.print_recipe());*/