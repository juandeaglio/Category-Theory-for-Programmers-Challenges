# Challenges
1. Implement, as best as you can, the identity function in your favorite language (or the second favorite, if your favorite language
happens to be Haskell). [Identity code](test_identity_function.py)
2. Implement the composition function in your favorite language. It
takes two functions as arguments and returns a function that is
their composition. [Composition code](test_compose_functions.py)
3. Write a program that tries to test that your composition function
respects identity. [Composition code](test_compose_functions.py)
4. Is the world-wide web a category in any sense? Are links 
morphisms? -- A world-wide web can have categories in it. If you imagine the 
web as a graph where a vertex is a website and an edge is a link
to/from the website, then you can describe the edges as morphisms.
The links are composable. For example, you can have an identity function 
where which takes an initial point, starting from a given website 
and end up at the same website through the links that are composed 
together. Links are morphisms if we abstract away all the 
underlying implementation and focus on the end result, i.e.
a new URL. The identity function would have a composable morphism
where the starting URL and the ending URL are equal, this is 
an example of isomorphism or invertibility.
5. Is Facebook a category, with people as objects and friendships as
morphisms? -- Yes, it contains categories in the same sense as a 
webpage, this graph is analogous in that the people are the vertices 
and the friendships are the edges that lead to different people. 
The friendships are composable, as you can start from your own 
Facebook profile, navigate to your friend, and arrive at your own 
Facebook profile by viewing their friends, an identity function 
(isomorphism, invertibility). However, not all Facebook users are 
in the same category of friends(they're all friends with each other)
but perhaps the viewpoint here is they're all Facebook users.
6. When is a directed graph a category?
A directed graph is a category for 1...n amount of nodes and 0...n nodes.
A trivial category would be 1 vertex with 0 edges, or perhaps an edge 
to itself. Something like the www or Facebook would need vertices and
edges such that you can form composable edges that are identity
functions.

# Examples 
### An example of identity function in C++:
`template<class T> T id(T x) { return x; }`

### and in Haskell:
`id :: a -> a`
`id x = x`
