import type { PageLoad } from "./$types";

export const load: PageLoad = async ({ params }) => {
	const id = params.id;
	const endpoint = `http://localhost:5000/boardgame/${id}`;

	try {
		const res = await fetch(endpoint);
		if (res.ok) {

            // console.log({ boardgame: await res.json() })
			return { boardgame: await res.json() };
		} else {
			console.error("Failed to fetch boardgame:", res.statusText);
			return { boardgame: null };
		}
	} catch (error) {
		console.error("Error loading boardgame:", error);
		return { boardgame: null };
	}
};
