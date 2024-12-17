<script lang="ts">
	import 'bootstrap/dist/css/bootstrap.min.css';
	import 'bootstrap-icons/font/bootstrap-icons.min.css';
	import { onMount } from 'svelte';
	import type { Boardgame } from '$lib/types/Boardgame';

	let boardgames: Boardgame[] = [];

	async function loadBoardgames() {
		const endpoint = 'http://localhost:5000/boardgame';
		try {
			const result = await fetch(endpoint);
			if (result.ok) {
				const data = await result.json();
				console.log('Fetched boardgames:', data);
				return Array.isArray(data) ? data : [];
			} else {
				console.error('Failed to fetch boardgames:', result.statusText);
				return [];
			}
		} catch (error) {
			console.error('Error loading boardgames:', error);
			return [];
		}
	}

	onMount(async () => {
		boardgames = await loadBoardgames();
	});
</script>

<div class="container mt-5">
	{#if boardgames.length > 0}
		<div class="row">
			{#each boardgames as boardgame}
				<div class="col-md-3 mb-5">
					<a href="boardgame/{boardgame.id}">
						<div class="card shadow">
							<div class="ratio ratio-4x3">
							<img
								src="http://cdn.shopify.com/s/files/1/0274/9631/products/pic2891964_1024x1024.jpg?v=1469169553"
								class="card-img-top"
								alt="..."
							/>
							</div>
							<div class="card-body">
								<h5 class="card-title">{boardgame.title}</h5>
							</div>
							<ul class="list-group list-group-flush">
								<li class="list-group-item">
									<div class="d-flex justify-content-between">
										<i class="bi bi-bookmark">kategória</i>
										{boardgame.category}
									</div>
								</li>
								<li class="list-group-item">
									<div class="d-flex justify-content-between">
										<i class="bi bi-people-fill">játékos</i>
										{boardgame.min_players} - {boardgame.max_players}
									</div>
								</li>
								<li class="list-group-item">
									<div class="d-flex justify-content-between">
										<i class="bi bi-person-fill-check">legjobb játékosszám</i>
										{boardgame.best_players}
									</div>
								</li>
								<li class="list-group-item">
									<div class="d-flex justify-content-between">
										<i class="bi bi-alarm-fill">átlagos játékidő</i>
										{boardgame.avg_time} perc
									</div>
								</li>
							</ul>
						</div>
					</a>
				</div>
			{/each}
		</div>
	{:else}
		<div class="container text-center mt-5 position-absolute start-50 translate-middle">
			<div class="card">
				<div class="card-header">Loading</div>
				<div class="card-body">
					<div class="spinner-border text-primary" role="status">
						<span class="visually-hidden">Betöltés...</span>
					</div>
				</div>
			</div>
		</div>
	{/if}
</div>
