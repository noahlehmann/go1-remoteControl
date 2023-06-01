<script>
    import { onMount } from 'svelte';
    import io from 'socket.io-client';
    import {writable} from "svelte/store";

    let socketConnected = false;
    const lastPressed = writable("None");
    let socket;

    function onKeyDown(e) {
        lastPressed.set(e.key);
        switch(e.key) {
            case "ArrowUp":
                socket.emit("keydown", "r_up")
                break;
            case "ArrowDown":
                socket.emit("keydown", "r_down")
                break;
            case "ArrowLeft":
                socket.emit("keydown", "r_left")
                break;
            case "ArrowRight":
                socket.emit("keydown", "r_right")
                break;
            case "w":
                socket.emit("keydown", "l_up")
                break;
            case "s":
                socket.emit("keydown", "l_down")
                break;
            case "a":
                socket.emit("keydown", "l_left")
                break;
            case "d":
                socket.emit("keydown", "l_right")
                break;
        }
    }

    function onKeyUp(e) {
        switch(e.key) {
            case "ArrowUp":
                socket.emit("keyup", "r_up")
                break;
            case "ArrowDown":
                socket.emit("keyup", "r_down")
                break;
            case "ArrowLeft":
                socket.emit("keyup", "r_left")
                break;
            case "ArrowRight":
                socket.emit("keyup", "r_right")
                break;
            case "w":
                socket.emit("keyup", "l_up")
                break;
            case "s":
                socket.emit("keyup", "l_down")
                break;
            case "a":
                socket.emit("keyup", "l_left")
                break;
            case "d":
                socket.emit("keyup", "l_right")
                break;
        }
    }

    onMount(() => {
        socket = io('http://localhost:5000'); // Replace with your server URL
        socket.on('connect', function() {
            socketConnected = true;
            socket.emit('my event', {data: 'I\'m connected!'});
        });

        return () => {
            socket.disconnect();
            socketConnected = false;
        };
    });
</script>

<svelte:head>
    <title>Home</title>
    <meta name="description" content="Svelte demo app"/>
</svelte:head>

<section>
    <p>
        {#if socketConnected}
            Connected
        {:else}
            Connecting...
        {/if}
    </p>
    <p>{$lastPressed}</p>
</section>

<style>
    section {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        flex: 0.6;
    }
</style>

<svelte:window on:keydown|preventDefault={onKeyDown} on:keyup|preventDefault={onKeyUp}/>
