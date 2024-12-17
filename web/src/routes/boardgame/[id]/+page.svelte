<script lang="ts">
	import type { Boardgame } from "$lib/types/Boardgame";

	export let data: { boardgame: Boardgame | null };
</script>

{#if data.boardgame}
<div class="container mt-4">
    <h1 class="pb-4">{data.boardgame.title}</h1>

    <div class="d-flex flex-row">
        {#each data.boardgame.tags.split(',') as tag}
            <h4><span class="badge bg-primary me-1">{ tag }</span></h4>
        {/each}
    </div>

    <div class="row">
        <div class="col-md-5 pb-4">
            <!-- Set a fixed aspect ratio for the image -->
            <div class="ratio ratio-1x1">
                <img
                    class="rounded shadow-lg"
                    src="http://cdn.shopify.com/s/files/1/0274/9631/products/pic2891964_1024x1024.jpg?v=1469169553"
                    alt="..."
                    width="100%"
                    height="100%"
                />
            </div>
        </div>

        <div class="col-md-7 pb-4">
            <!-- List Group -->
            <ul class="list-group pb-4">
                <li class="list-group-item active">Játék adatok</li>
                <li class="list-group-item">
                    <div class="d-flex justify-content-between">
                        <p>kategória</p>
                        <p>{data.boardgame.category}</p>
                    </div>
                </li>
                <li class="list-group-item">
                    <div class="d-flex justify-content-between">
                        <p>Játékos szám</p>
                        <p>{data.boardgame.min_players} - {data.boardgame.max_players} fő</p>
                    </div>
                </li>
                <li class="list-group-item">
                    <div class="d-flex justify-content-between">
                        <p>Legjobb játékosszám</p>
                        <p>{data.boardgame.best_players} fő</p>
                    </div>
                </li>
                <li class="list-group-item">
                    <div class="d-flex justify-content-between">
                        <p>Átlagos játékidő</p>
                        <p>{data.boardgame.avg_time} perc</p>
                    </div>
                </li>
            </ul>

            <!-- Description section -->
            <ul class="list-group">
                <li class="list-group-item active">Leírás</li>
                <li class="list-group-item">
                    <div class="description-wrapper overflow-auto">
                        {data.boardgame.description}
					</div>
                </li>
            </ul>
        </div>
    </div>
</div>
{/if}
