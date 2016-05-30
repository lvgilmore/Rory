THIS repository if for the development of the next version of Rory,
because we all appreciate her eyes.

In this version our primary goal is to let Rory "install" hosts who
already have an OS because they've been deployed from image/template
To do so we assume that they'll have a service, as part of their
image, who'll make them register through an API to Rory.

Our secondary goal is to make Rory more maintainable by adding logs
and appropriate exceptions.


workflow breakdown:
1. client sends "hello"
	we learn its ip, save its fingerpring, etc
2. discovery
	each ego learn what it needs to make build the host's "ego"
	e.g. puppet ego learns ssl cert, basic ego learns hostname
3. backend conf
	each ego adds the host the its backend
	e.g. puppet ego signs the cert, basic ego register to DNS
4. node conf
	echo ego configure the node
	e.g. puppet ego register relevant groups, basic ego runs script, etc.