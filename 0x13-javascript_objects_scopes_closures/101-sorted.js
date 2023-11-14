#!/usr/bin/node

const {dict} = require("./101-data.js");
set = new Set(Object.values(dict));
let newdict = {}
for (let i of set) {
	let list = [];
	for (let k of Object.keys(dict)) {
		if (dict[k] === i) {
		list.push(`${k}`)
		}
	newdict[i.toString()] = list;
	}
}
console.log(newdict);
