<script>
    import { onMount } from 'svelte';
    import io from 'socket.io-client';
    import {writable} from "svelte/store";
    import ArrowControl from "./ArrowControl.svelte";
    import CameraPicture from "./CameraPicture.svelte";

    let socketConnected = false;
    const lastPressed = writable("None");
    let socket;

    let letters, arrows;

    function onKeyDown(e) {
        lastPressed.set(e.key);
        switch(e.key) {
            case "ArrowUp":
                socket.emit("keydown", "r_up")
                arrows.highlight({up: true})
                break;
            case "ArrowDown":
                socket.emit("keydown", "r_down")
                arrows.highlight({down: true})
                break;
            case "ArrowLeft":
                socket.emit("keydown", "r_left")
                arrows.highlight({left: true})
                break;
            case "ArrowRight":
                socket.emit("keydown", "r_right")
                arrows.highlight({right: true})
                break;
            case "w":
                socket.emit("keydown", "l_up")
                letters.highlight({up: true})
                break;
            case "s":
                socket.emit("keydown", "l_down")
                letters.highlight({down: true})
                break;
            case "a":
                socket.emit("keydown", "l_left")
                letters.highlight({left: true})
                break;
            case "d":
                socket.emit("keydown", "l_right")
                letters.highlight({right: true})
                break;
        }
    }

    function onKeyUp(e) {
        switch(e.key) {
            case "ArrowUp":
                socket.emit("keyup", "r_up")
                arrows.highlight({up: false})
                break;
            case "ArrowDown":
                socket.emit("keyup", "r_down")
                arrows.highlight({down: false})
                break;
            case "ArrowLeft":
                socket.emit("keyup", "r_left")
                arrows.highlight({left: false})
                break;
            case "ArrowRight":
                socket.emit("keyup", "r_right")
                arrows.highlight({right: false})
                break;
            case "w":
                socket.emit("keyup", "l_up")
                letters.highlight({up: false})
                break;
            case "s":
                socket.emit("keyup", "l_down")
                letters.highlight({down: false})
                break;
            case "a":
                socket.emit("keyup", "l_left")
                letters.highlight({left: false})
                break;
            case "d":
                socket.emit("keyup", "l_right")
                letters.highlight({right: false})
                break;
        }
    }

    onMount(() => {
        socket = io('http://localhost:5000'); // Replace with your server URL
        socket.on('connect', function() {
            socketConnected = true;
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
<svelte:window on:keydown|preventDefault={onKeyDown} on:keyup|preventDefault={onKeyUp}/>

<section>
    <div class="top-container">
        <ArrowControl bind:this={letters}/>
        <CameraPicture/>
        <ArrowControl bind:this={arrows}/>
    </div>
</section>

<style>
    section {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .top-container {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-evenly;
    }
</style>


