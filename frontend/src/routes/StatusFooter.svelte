<div class="container">
    <div class="status-container">
        <p class="status-text">
            {#if true}
                Connected
            {:else}
                Connecting...
            {/if}
        </p>
    </div>

</div>

<style>
    .container {
        display: flex;
        flex-direction: row-reverse;
        padding: 5em;
    }
    .status-container {
        padding-left: 1em;
        padding-right: 1em;
        border-radius: 1em;
        border: 1px solid black;
    }
</style>