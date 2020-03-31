/*var count=0;
function Results()
{
	document.getElementById('container').remove();
	var body=document.getElementById('Body');
	let container=document.createElement('div');
	container.setAttribute('id','container');
	container.setAttribute('class','container');
	for(let i=0;i<4;i++)
	{
		var row=document.createElement('div');
		row.setAttribute('id','row');
		row.setAttribute('class','row');
		for(let j=0;j<3;j++)
		{
			var col=document.createElement('div');
			var title=document.createTextNode('{{ context["title"]}}')
			col.setAttribute('id','col');
			col.setAttribute('class','col-md-4');
			col.setAttribute('onclick','popup()');
			var card=document.createElement('div');
			card.setAttribute('id','card');
			card.setAttribute('class','card');
			card.appendChild(title)
			col.appendChild(card);
			row.appendChild(col);
		}
		container.appendChild(row);
	}
	body.appendChild(container);
	let morediv=document.createElement('center');
	let more=document.createElement('button');
	let text=document.createTextNode('More Results');
	more.appendChild(text);
	more.setAttribute('id','more');
	more.setAttribute('class','btn btn-danger');
	more.setAttribute('onclick','MoreResult()');
	morediv.appendChild(more);
	container.appendChild(morediv);
}
function MoreResult()
{
	count++;
	document.getElementById('more').remove();
	var body=document.getElementById('Body');
	container=document.getElementById('container');
	for(let i=0;i<4;i++)
	{
		var row=document.createElement('div');
		row.setAttribute('id','row');
		row.setAttribute('class','row');
		for(let j=0;j<3;j++)
		{
			var col=document.createElement('div');
			col.setAttribute('id','col');
			col.setAttribute('class','col-md-4');
			col.setAttribute('onclick','popup()');
			var card=document.createElement('div');
			card.setAttribute('id','card');
			card.setAttribute('class','card');
			col.appendChild(card);
			row.appendChild(col);
		}
		container.appendChild(row);
	}
	body.appendChild(container);
	if(count<3)
	{
		let more=document.createElement('button');
		let morediv=document.createElement('center');
		let text=document.createTextNode('More Results');
		more.appendChild(text);
		more.setAttribute('id','more');
		more.setAttribute('class','btn btn-danger');
		more.setAttribute('onclick','MoreResult()');
		morediv.appendChild(more);
		container.appendChild(morediv);
	}
}*/
function popup()
{
	console.log("hello");
	css=document.getElementById('sec');
	css.style.display = "block";
}