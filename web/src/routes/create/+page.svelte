<script lang="ts">
	import type { Boardgame } from '$lib/types/Boardgame';
	import type { BoardgameCreate } from '$lib/types/BoardgameCreate';

	const endpoint = `http://localhost:5000/boardgame`;

	let newTag: string = '';
	let tags: string[] = ['asdasdasdasdsad', 'asdasdsad', 'asdasdd', 'asd', 'dsa'];

	// Form fields
	let title: string = '';
	let category: string = '1';
	let minPlayers: number = 1;
	let maxPlayers: number = 5;
	let bestPlayers: number = 3;
	let minAge: number = 12;
	let avgTime: number = 30;
	let description: string = '';

	// Validation state
	let errors = {
		title: false,
		description: false,
		minMaxPlayers: false
	};

	function addTag(name: string) {
		if (name.trim()) {
			if (!tags.includes(name)) {
				tags = [...tags, name];
			}
			newTag = '';
		}
	}

	function removeTag(name: string) {
		tags = tags.filter((tag) => tag !== name);
	}

	function validateForm() {
		let isValid = true;

		// Reset errors
		errors = { title: false, description: false, minMaxPlayers: false };

		// Title validation
		if (!title.trim()) {
			errors.title = true;
			isValid = false;
		}

		// Description validation
		if (!description.trim()) {
			errors.description = true;
			isValid = false;
		}

		// Min/Max players validation
		if (minPlayers > maxPlayers) {
			errors.minMaxPlayers = true;
			isValid = false;
		}

		return isValid;
	}

	async function saveBoardgame(event: Event) {
		event.preventDefault(); // Prevent default form submission

		if (validateForm()) {
			console.log('Form is valid!');

			let boardgame: BoardgameCreate = {
				title: title,
				category: category,
				description: description,
				tags: tags.toString(),
				min_players: minPlayers,
				max_players: maxPlayers,
				best_players: bestPlayers,
				min_age: minAge,
				avg_time: avgTime
			};

			console.log(boardgame);

			try {
				const res = await fetch(endpoint, {
					method: 'POST',
					body: JSON.stringify(boardgame),
					headers: {
						'Content-Type': 'application/json'
					}
				});

				if (res.ok) {
					alert('Sikeres mentés!');
				} else {
					console.error('Failed to fetch boardgame:', res.statusText);
				}
			} catch (error) {
				console.error('Error loading boardgame:', error);
			}
		} else {
			console.log('Form validation failed!');
		}
	}
</script>

<div class="test-border container my-4">
	<form class="row g-3 needs-validation" novalidate on:submit|preventDefault={saveBoardgame}>
		<!-- Title Input -->
		<div class="form-group col-md-6">
			<label for="title">Név</label>
			<input
				bind:value={title}
				type="text"
				class="form-control {errors.title ? 'is-invalid' : ''}"
				id="title"
				placeholder="Név"
				required
			/>
			{#if errors.title}
				<div class="invalid-feedback">A név megadása kötelező!</div>
			{/if}
		</div>

		<!-- Category Select -->
		<div class="form-group col-md-3">
			<label for="category">Kategória</label>
			<select bind:value={category} class="form-select" id="category">
				<option value="1">party</option>
				<option value="2">családi</option>
				<option value="3">stratégia</option>
				<option value="4">gyerek</option>
				<option value="5">haladó</option>
				<option value="6">gamer</option>
				<option value="7">szó</option>
				<option value="8">kártya</option>
			</select>
		</div>

		<!-- Min/Max Players -->
		<div class="form-group col-md-3">
			<label for="minPlayers">Játékosszám (min)</label>
			<input bind:value={minPlayers} type="number" min="1" max="99" class="form-control" />
		</div>

		<div class="form-group col-md-3">
			<label for="maxPlayers">Játékosszám (max)</label>
			<input
				bind:value={maxPlayers}
				type="number"
				min="1"
				max="99"
				class="form-control {errors.minMaxPlayers ? 'is-invalid' : ''}"
			/>
			{#if errors.minMaxPlayers}
				<div class="invalid-feedback">
					A maximum játékosszám nagyobb kell legyen, mint a minimum!
				</div>
			{/if}
		</div>

		<!-- Best Player Count -->
		<div class="form-group col-md-3">
			<label for="bestPlayers">Játékosszám (legjobb)</label>
			<input bind:value={bestPlayers} type="number" min="1" max="99" class="form-control" />
		</div>

		<!-- Age -->
		<div class="form-group col-md-3">
			<label for="minAge">Minimum életkor</label>
			<input bind:value={minAge} type="number" min="1" max="99" class="form-control" />
		</div>

		<!-- Avg Time -->
		<div class="form-group col-md-3">
			<label for="avgTime">Átlagos idő (perc)</label>
			<input bind:value={avgTime} type="number" min="1" max="200" class="form-control" />
		</div>

		<!-- Tags -->
		<div class="form-group col-md-3">
			<label for="tags">Tag</label>
			<div class="input-group">
				<input bind:value={newTag} type="text" class="form-control" placeholder="Tag név" />
				<button class="btn btn-outline-primary" type="button" on:click={() => addTag(newTag)}>
					Hozzáadás
				</button>
			</div>
		</div>

		<div class="form-group col-md-12 test-border">
			{#each tags as tag}
				<button type="button" class="btn btn-primary m-1" on:click={() => removeTag(tag)}>
					{tag}
				</button>
			{/each}
			{#if tags.length > 0}
				<div class="alert alert-secondary mt-1" role="alert">
                    Tag törléséhez kattints a dobozára.
                </div>
			{/if}
		</div>

		<!-- Description -->
		<div class="form-group col-md-12">
			<label for="description" class="form-label">Játék leírása</label>
			<textarea
				bind:value={description}
				class="form-control {errors.description ? 'is-invalid' : ''}"
				id="description"
				rows="6"
			></textarea>
			{#if errors.description}
				<div class="invalid-feedback">A leírás megadása kötelező!</div>
			{/if}
		</div>

		<!-- Submit Button -->
		<div class="test-border col">
			<button type="submit" class="btn btn-primary">Mentés</button>
		</div>
	</form>
</div>

<style>
	.test-border {
		border: 0px solid red;
	}
</style>
